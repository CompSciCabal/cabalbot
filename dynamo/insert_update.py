import boto3
from query import diversion_for_week, diversion_for_week_paper

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Diversions')

def add_unscheduled_paper(paperURI):
    """Add a new paper to be scheduled."""
    resp = table.put_item(
        Item={
            "WeekOf": "unscheduled", "Available": [], "Unavailable": [],
            "Attendees": [], "Activity": "reading", "ActivityDetails": {},
            "Paper": paperURI, "Interested": [], "NotInterested": [],
            "HaveRead": [], "Ratings": {}
        })

    return resp

def add_interest_paper(date, paperURI, user):
    """Indicate interest in the given paper for the given user. A user cannot be
    interested and not intersted in the same paper."""
    paper = diversion_for_week_paper(date, paperURI)
    not_interested = paper['NotInterested']
    if user in not_interested:
        not_interested.remove(user)
    interested = paper['Interested']
    if user not in interested:
        interested.append(user)
        resp = table.update_item(
            Key={"WeekOf": date, "Paper": paperURI},
            ExpressionAttributeNames={
                "#interested": "Interested",
                "#notInterested": "NotInterested"
            },
            ExpressionAttributeValues={
                ":interested": interested,
                ":notInterested": not_interested
            },
            UpdateExpression="SET #interested = :interested, #notInterested = :notInterested"
        )

def add_disinterest_paper(date, paperURI, user):
    """Similar to add_interest_paper."""
    paper = diversion_for_week_paper(date, paperURI)
    interested = paper['Interested']
    if user in interested:
        interested.remove(user)
    not_interested = paper['NotInterested']
    if user not in not_interested:
        not_interested.append(user)
        resp = table.update_item(
            Key={"WeekOf": date, "Paper": paperURI},
            ExpressionAttributeNames={
                "#interested": "Interested",
                "#notInterested": "NotInterested"
            },
            ExpressionAttributeValues={
                ":interested": interested,
                ":notInterested": not_interested
            },
            UpdateExpression="SET #interested = :interested, #notInterested = :notInterested"
        )

def remove_interest_paper(date, paperURI, user):
    """Remove user's interest in the given paper. A user can be neither interested nor
    not interested in a paper; cabalbot does not mind fear of commitment."""
    paper = diversion_for_week_paper(date, paperURI)
    interested = paper['Interested']
    if user in interested:
        interested.remove(user)
        resp = table.update_item(
            Key={"WeekOf": date, "Paper": paperURI},
            ExpressionAttributeNames={
                "#interested": "Interested"
            },
            ExpressionAttributeValues={
                ":value": interested
            },
            UpdateExpression="SET #interested = :value"
        )

def remove_disinterest_paper(date, paperURI, user):
    """Similar to remove_interest_paper."""
    paper = diversion_for_week_paper(date, paperURI)
    not_interested = paper['NotInterested']
    if user in not_interested:
        not_interested.remove(user)
        resp = table.update_item(
            Key={"WeekOf": date, "Paper": paperURI},
            ExpressionAttributeNames={
                "#notInterested": "NotInterested"
            },
            ExpressionAttributeValues={
                ":value": not_interested
            },
            UpdateExpression="SET #notInterested = :value"
        )

def add_read_paper(date, paperURI, user):
    """Indicate that user has read / is reading the given paper."""
    paper = diversion_for_week_paper(date, paperURI)
    readers = paper['HaveRead']
    if user not in readers:
        readers.append(user)
        resp = table.update_item(
            Key={"WeekOf": date, "Paper": paperURI},
            ExpressionAttributeNames={
                "#readers": "HaveRead"
            },
            ExpressionAttributeValues={
                ":value": readers
            },
            UpdateExpression="SET #readers = :value"
        )

def add_rating_paper(date, paperURI, user, rating):
    """Add a rating for the given paper by the given user."""
    paper = diversion_for_week_paper(date, paperURI)
    ratings = paper['Ratings']
    if (user not in ratings) or (ratings[user] != rating):
        resp = table.update_item(
            Key={"WeekOf": date, "Paper": paperURI},
            ExpressionAttributeNames={
                "#ratings": "Ratings",
                "#user": user
            },
            ExpressionAttributeValues={
                ":value": rating
            },
            UpdateExpression="SET #ratings.#user = :value"
        )

def add_availability_week(date, user):
    """Indicate that user is available on the given week."""
    diversions = diversion_for_week(date)
    for diversion in diversions:
        unavailable = diversion['Unavailable']
        if user in unavailable:
            unavailable.remove(user)
        available = diversion['Available']
        if user not in available:
            available.append(user)
            resp = table.update_item(
                Key={"WeekOf": date, "Paper": diversion['Paper']},
                ExpressionAttributeNames={
                    "#available": "Available",
                    "#unavailable": "Unavailable"
                },
                ExpressionAttributeValues={
                    ":available": available,
                    ":unavailable": unavailable
                },
                UpdateExpression="SET #available = :available, #unavailable = :unavailable"
            )

def add_unavailability_week(date, user):
    """Indicate that user is unavailable on the given week."""
    diversions = diversion_for_week(date)
    for diversion in diversions:
        available = diversion['Available']
        if user in available:
            available.remove(user)
        unavailable = diversion['Unavailable']
        if user not in unavailable:
            unavailable.append(user)
            resp = table.update_item(
                Key={"WeekOf": date, "Paper": diversion['Paper']},
                ExpressionAttributeNames={
                    "#available": "Available",
                    "#unavailable": "Unavailable"
                },
                ExpressionAttributeValues={
                    ":available": available,
                    ":unavailable": unavailable
                },
                UpdateExpression="SET #available = :available, #unavailable = :unavailable"
            )
