Ideas for commands! Syntax loosely inspired by http://daimio.org, because why not.

`/cabalbot eat paper [url]`  
Adds the paper to the list

`/cabalbot list papers`  
Returns a list of papers (id, url, title, likes, dislikes, schedule, etc)

`/cabalbot like paper [url/id]`  
Tells cabalbot that you would like to read that paper  
The cabalbot will try to schedule that paper on a week you are available

`/cabalbot dislike paper [url/id]`  
Tells cabalbot you are not interested in that paper  
It will try to schedule it during a week you are not attending

`/cabalbot schedule for [week]`  
Returns the schedule for the week, or "Not yet scheduled"  
Once scheduled, the schedule for a given week is relatively constant

`/cabalbot what are we doing tonight`  
Alias for `/cabalbot schedule for this week`

`/cabalbot attending on [week]`  
Tells cabalbot you will be attending that week, so it can schedule fun things for you

`/cabalbot absent on [week]`  
Asks cabalbot not to schedule fun things for you that week, because you will be gone

`/cabalbot I'm reading [url/id]`  
Tells cabalbot you are reading a paper. Cabalbot will add it to its list, and might schedule a short presentation from you on it.

`/cabalbot I'm bored`  
Your friendly cabalbot cares about you, and wants you to live a full, exciting life. You'll be assigned a paper to read, and a short presentation on it will be scheduled in the near future.

TODOS:
- We should add tasks like group programming, demos, etc in addition to papers. 
- There ought to be a way to reschedule an upcoming session for holidays etc. 

Otherwise I think everything is perfect and our cabalbot is going to be our best friend and new supreme robot overlord. All hail cabalbot!


