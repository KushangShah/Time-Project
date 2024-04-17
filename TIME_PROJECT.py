# Creating a class called time
class Time:

    def __init__(self, hour, minute):
        # assigning hour and minute to self parameter
        self.hour = hour
        self.minute = minute

    # Displaying display to show time in AM and PM
    def DisplayTime(self):
        try:
            # hour and minute should not be more than 24 hours and 60 minute
            if self.hour >= 23:
                print("Hour should not be more than 24 hours")
                return
            
            if self.minute >= 59:
                print("Minute should not be greater than 60 minute")
                return
            
            #  if hour more than 12 it's PM else Am
            if self.hour >= 12:
                am_pm = "PM"
                if self.hour > 12:
                    self.hour -= 12

            if self.hour < 12:
                am_pm = "AM"
                if self.hour == 0:
                    self.hour = 12
            print(f"The Time is {self.hour}:{self.minute} {am_pm}")
        except ZeroDivisionError:
            print("An error occured")

    # Defing ratio of min/hour
    def DisplayRatio(self):
        try:
            ratio = self.minute / self.hour
        except Exception as e:
            print(f"An error occured: {e}")

# Output

