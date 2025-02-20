spdlim = int(input("Enter the speed limit: "))
spd = int(input("Enter the recorded speed of the car: "))

if (spd - spdlim <= 0):
    print("Congratulations, you are within the speed limit!")
else:
    fine = 0
    if (1 <= spd - spdlim <= 20):
        fine = 100
    if (21 <= spd - spdlim <= 30):
        fine = 270
    if (spd - spdlim >= 31):
        fine = 500
    print("You are speeding and your fine is ${}.".format(fine))