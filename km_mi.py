print("How many kilometers did you run today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms} km run is equal to {miles} mi")

# round(thing to round, how many decimal points)