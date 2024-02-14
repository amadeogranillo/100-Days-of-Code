welcome = input("Welcome! What is your name?")
print("Hello " + welcome)
ask_hours = input("Please enter the number of hours you worked")
ask_rate = input("What is your rate per hour?")

try:

    ah = float(ask_hours)
    ar = float(ask_rate)

    def computepay(hours, rate):
        if hours > 40:
            # Overtime
            reg = (hours * rate)
            otp = (hours - 40.0) * (rate * 0.5)
            # print reg,otp
            return reg + otp
        else:
            return hours * rate
except:
       print("Error,input numeric value on both fields")
       quit()

print("Pay", computepay(ah,ar))




