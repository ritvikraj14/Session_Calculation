# Session_Calculation


This program will calculate the total and valid number of sessions per user of game.

Calculation strategy:

1. First calculate the events belongs to user
2. Sort those events w.r.t time
3. Then search for first "ggstart" event
4. Now check the time difference between current and previous event
    
    a. If time difference is less than 30 secs then that event is included in current session
    
    b. If time difference is greater than 30 then it will check the following conditions
    
        i) if previous and current events are "ggstop" then break the session
        
        ii) if previous event is "ggstop" and current is "ggstart" then break the session
        
        iii) if previous and current both are "ggstart" events then break
        
        iv) else continue;
        
    c. Session time is calculated by taking time difference between start and end event. So if
        session time is greater than 60 then that session is considered as valid session and if
        session time greater than 1 and less than 60 then it is invalid session.
        
    d. Average session time is calculated.


# User insights:

User dictionary or device history can give us information that which game is mostly played by user.


# Data insights:

Attributes debug, random, and params are not required because they are empty most of time.

## To run program:
#  Requirements:

1. Python3
2. data file

```python
python3 run.py --help # for help

python3 run.py -f ggevent.log -o output.txt
```
