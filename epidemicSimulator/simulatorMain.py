import simulatorIntro
import GuiHandler
import ActionHandler


#set up people Gui and the number according to the user
GuiHandler.setPeople(simulatorIntro.numberOfPeople)
#set the infection time specified by the user
ActionHandler.infectionTime = simulatorIntro.infectionTime
#set the infection radius specified by the user
ActionHandler.radius = simulatorIntro.radius

#loop through the 1 - percentage and add those numbers to the list
for i in range(1,simulatorIntro.percentage):
    ActionHandler.randIList.append(i)

#spawn patient zero and set the GUI
ActionHandler.spawnPatientZero()

#choose which simulation to run
if simulatorIntro.choice == "S":
    ActionHandler.socialDistance()
elif simulatorIntro.choice == "R":
    ActionHandler.randomWalk()
