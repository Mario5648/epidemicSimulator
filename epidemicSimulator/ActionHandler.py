import GuiHandler
import random
import graph

infected = [] #List that will contain the people that are infected
infectedDays = {} # This will have a key being the person object and the value of being how many days they have been infected
safe = [] # Once they have experienced the amount of days with the virus they will then be safe from recontracting the virus
infectionTime = 0  # how many days does the virus last in host
randIList = [] # This will be populated with numbers 1-100 depending on percentage
radius = 0 # the radius where the virus can spread

#Set up patient zero
def spawnPatientZero():
    GuiHandler.setPatientZero()
    infectedDays[GuiHandler.patient0] = 0
    infected.append(GuiHandler.patient0)

#Check if the current person is near an infected person
def nearInfectedCheck(person):
    #loop through all infected people
    for infec in infected:
        #if a person is not in the safe list then continue
        if person not in safe:
            #generate a number
            randI = random.randint(1,100)
            #check a number is in the randIList to see if the person will get infected
            #percentage
            if randI in randIList:
                # if the person is in the radius then infect them
                if (person.xcor() <= infec.xcor()+radius and person.xcor() >= infec.xcor()-radius) and (person.ycor() >= infec.ycor()-radius and person.ycor() <= infec.ycor()+radius):
                    #change the color to be red
                    person.color("red")
                    #give them start day and add them to infected list
                    infected.append(person)
                    infectedDays[person] = 0
                    break
#Check if the person can recover or if they still have days left
def recover(person):
    #if the person is infected then check
    if person in infectedDays:
        if person in infected:
            #if the person still has remaing days then increment their days
            if infectedDays[person] != infectionTime * 5:
                infectedDays[person] += 1
                return 1
            #if the person has experieced the full infection duration then recover them
            elif infectedDays[person] == infectionTime * 5:
                person.color("blue")
                infected.remove(person)
                del infectedDays[person]
                safe.append(person)
                return 2
    return 3
#check if there are people infected
#if no more infected then the simulation will terminate
def infectionCheck():
    if len(infected) == 0:
        return True

#if someone is near  a person then they will want to move away from them
#this is used for the social distancing algorithm
def nearSomeone(person):
    #check all people
    for p in GuiHandler.people:
        #if they are in the radius then move them
            if (person.xcor() <= p.xcor()+70 and person.xcor() >= p.xcor()-70) and (person.ycor() >= p.ycor()-70 and person.ycor() <= p.ycor()+70):
                y = random.randint(-30,30)
                person.dy = y
                person.sety(person.ycor()+person.dy)

                x = random.randint(-30,30)
                person.dx = x
                person.setx(person.xcor()+person.dx)

                break


#Social distancing algorithm

# this algorithms simulates social distancing by moving people further if they are
#currently near someone

#the people will also walk shorter distances since they have to be aware of
#their surrondings
def socialDistance():
    #clock is used to increment to get the number of days to export to the graph
    #every 5 iterations is a day
    clock = 0
    #dataset will send the data to the graph function [days,healthy,infected,recovered]
    dataset = []
    while True:
        GuiHandler.wn.update()
        #loop through everyone
        for person in GuiHandler.people:
            #randomly choose where the current person will walk
            direction = random.randint(0,1)
            if direction == 0:
                y = random.randint(-5,5)
                person.dy = y
                person.sety(person.ycor()+person.dy)
            else:
                x = random.randint(-5,5)
                person.dx = x
                person.setx(person.xcor()+person.dx)

            #if the person is recovered then dont bother executing the rest of the code
            if recover(person) == 1 or recover(person) == 2:
                continue
            #check if they are near someone so they can move
            nearSomeone(person)
            #check if they are infected to determine if they will be infected
            nearInfectedCheck(person)
        #move patient zero
        if direction == 0:
            x0 = random.randint(-5,5)
            GuiHandler.patient0.setx(GuiHandler.patient0.xcor()+x0)
        else:
            y0 = random.randint(-5,5)
            GuiHandler.patient0.sety(GuiHandler.patient0.ycor()+y0)
        #check if patient zero can recover
        recover(GuiHandler.patient0)

        clock += 1
        #add the current information to dataset
        dataset.append([clock,(len(GuiHandler.people)-(len(infected)+len(safe))),len(infected),len(safe)])
        #if all infected people are gone then terminate the simulation
        if infectionCheck():
            break
    #send dataset to graph.py inorder to plot
    graph.appendPlots(dataset)

#randomWalk algorithm

#This will simulate normal life. People are free to move and dont mind being
#next to eachother
def randomWalk():
    #clock is used to increment to get the number of days to export to the graph
    #every 5 iterations is a day
    clock = 0
    #dataset will send the data to the graph function [days,healthy,infected,recovered]
    dataset = []
    while True:
        GuiHandler.wn.update()
        #loop through everyone
        for person in GuiHandler.people:
            #randomly choose where the current person will walk
            direction = random.randint(0,1)
            if direction == 0:
                y = random.randint(-20,20)
                person.dy = y
                person.sety(person.ycor()+person.dy)
            else:
                x = random.randint(-20,20)
                person.dx = x
                person.setx(person.xcor()+person.dx)


            #if the person is recovered then dont bother executing the rest of the code
            if recover(person) == 1 or recover(person) == 2:
                continue

            #check if they are infected to determine if they will be infected
            nearInfectedCheck(person)


        #move patient zero
        if direction == 0:
            x0 = random.randint(-20,20)
            GuiHandler.patient0.setx(GuiHandler.patient0.xcor()+x0)
        else:
            y0 = random.randint(-20,20)
            GuiHandler.patient0.sety(GuiHandler.patient0.ycor()+y0)

        recover(GuiHandler.patient0)
        clock += 1
        #add the current information to dataset
        dataset.append([clock,(len(GuiHandler.people)-(len(infected)+len(safe))),len(infected),len(safe)])
        #if all infected people are gone then terminate the simulation
        if infectionCheck():
            break
    #send dataset to graph.py inorder to plot
    graph.appendPlots(dataset)
