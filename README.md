# Time-Project
The peace of code converts user input time in 24 hour format into 12 hour O'clock time. 

The input method should be like this: 
  input -->
    hour, minute
    eg..,
    (23,45)
  output -->
    The time is 11:45 PM

or if the user have multiple input time, then store them in list:
  for example -->
    hout_min_list = [(23,45), (34,50), (12,34), (14,67),(19,20), (2,15), (0, 10)]
.
    and simply copy and past this part ->
        for hour, minute in hour_min_list:
        t = Time(hour, minute)
        t.DisplayTime()
        t.DisplayRatio()
        print()
.
  Output will be like this:
    output -->
      The time is 11:45 PM
      Hour should be less then 24.     
      The time is 12:34 PM      
      Minutes should be less than 60.   
      The time is 7:20 PM     
      The time is 2:15 AM     
      The time is 12:10 AM

    
