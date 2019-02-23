Ideas for commands! Syntax loosely inspired by http://daimio.org, because why not.

`/cabalbot eat paper [url]`  
Sends the paper to cabalbot's ingestion engine

`/cabalbot want paper [url/id]`  
Tells cabalbot that you would like to read that paper  
The cabalbot will try to schedule that paper on a week you are available

`/cabalbot unwant paper [url/id]`  
Tells cabalbot you are not interested in that paper  
It will try to schedule it during a week you are not attending

`/cabalbot what are we doing tonight`  
Collapses the superimposition of schedules to provide a fun and stimulating set of activities for the evening

`/cabalbot attending on [week]`  
Tells cabalbot you will be attending that week, so it can schedule fun things for you

`/cabalbot absent on [week]`  
Asks cabalbot not to schedule fun things for you that week, because you will be gone

`/cabalbot I'm reading [url/id]`  
Tells cabalbot you are reading a paper. Cabalbot will add it to its list, and might schedule a short presentation from you on it.

`/cabalbot I'm bored`  
Your friendly cabalbot cares about you, and wants you to live a full, exciting life. You'll be assigned a paper to read, and a short presentation on it will be scheduled in the near future.

`/cabalbot judge paper [url/id] rating [rating]`  
Judgement Dimensions:  
Quality of paper?  
Amount of content?  
Did I understand it?  
Do I want to read more like it?  

Judgements are stored as strings of four characters, as follows:  
AAAA is a high quality paper with lots of content that you understood completely and would like to read more about.  
FFFF is a low quality paper with no content that you didn't understand and never want to see again.  
BCDF is a decent quality paper with some content that you only slightly understood and never want to see again.  
(The fact that these rating strings are also valid two byte hex strings is entirely incidental.)  


TODOS:
- We should add tasks like group programming, demos, etc in addition to papers. 
- There ought to be a way to reschedule an upcoming session for holidays etc. 

Otherwise I think everything is perfect and our cabalbot is going to be our best friend and new supreme robot overlord. All hail cabalbot!


