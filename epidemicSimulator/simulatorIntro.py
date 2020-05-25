import sys

#options
numberOfPeople = 0
infectionTime = 0
radius = 0
percentage = 0
choice = "N"


# choose how you want your disease to affect the people


while True:
    numberOfPeople = int(input("Enter The Amount Of People (Max:300 Min:2): "))
    if numberOfPeople < 301 and numberOfPeople > 1:
        break

while True:
    infectionTime = int(input("Enter The Amount Of Days The Infection Will Last (Max:20 Min:1): "))
    if infectionTime < 21 and infectionTime > 0:
        break
while True:
    radius = int(input("Enter The Radius Of Infection (Max:200 Min:1): "))
    if radius < 201 and radius > 0:
        break
while True:
    percentage = int(input("Enter The Probability Of Someone Getting Infected (Max:100 Min:1): "))
    if percentage < 101 and percentage > 0:
        break
while True:
    choice = input("Run Simulation With \"S\" (SocialDistancing) Or \"R\" (RandomWalk) : "  )
    if choice == "R" or choice == "S":
        break
