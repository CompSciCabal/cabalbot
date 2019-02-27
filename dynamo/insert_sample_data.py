# -*- coding: utf-8 -*-
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Diversions')

with table.batch_writer() as batch:
    batch.put_item(Item={"WeekOf": "2019-02-22", "Available": [], "Unavailable": ["scott"],
        "Attendees": ["dann", "jrootham", "inaimathi", "erik", "hzafar"],
        "Activity": "coding",
        "ActivityDetails": {"Repository": "https://github.com/CompSciCabal/cabalbot"},
        "Paper": "none",
        "Interested": [],
        "NotInterested": [],
        "HaveRead": [],
        "Ratings": {} })
    batch.put_item(Item={"WeekOf": "2019-03-01", "Available": [], "Unavailable": [],
        "Attendees": [],
        "Activity": "reading",
        "ActivityDetails": {"Title": u"Prototyping a Functional Language using Higher-Order Logic Programming: A Functional Pearl on Learning the Ways of λProlog/Makam"},
        "Paper": "http://adam.chlipala.net/papers/MakamICFP18/MakamICFP18.pdf",
        "Interested": ["dann"],
        "NotInterested": [],
        "HaveRead": [],
        "Ratings": {} })
    batch.put_item(Item={"WeekOf": "unscheduled", "Available": [], "Unavailable": [],
        "Attendees": [],
        "Activity": "reading",
        "ActivityDetails": {"Title": "Proofs of life: molecular-biology reasoning simulates cell behaviors from first principles"},
        "Paper": "http://arxiv.org/pdf/1811.02478.pdf",
        "Interested": ["dann"],
        "NotInterested": ["hzafar"],
        "HaveRead": [],
        "Ratings": {} })
