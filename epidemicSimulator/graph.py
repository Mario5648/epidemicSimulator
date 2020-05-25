import matplotlib.pyplot as plt


#recieve all the data from ActionHandler and plot it
def appendPlots(dataSet):
    xCoordinates = [] # days
    yCoordinates = [] #infected
    recCoordinates = [] # recovered
    healthyCoordinates = [] # healthy
    for data in dataSet:
        days = data[0]/5
        xCoordinates.append(days)
        healthy = data[1]
        healthyCoordinates.append(healthy)
        infected = data[2]
        yCoordinates.append(infected)
        recovered = data[3]
        recCoordinates.append(recovered)

    plt.plot(xCoordinates, yCoordinates, label = "Infected")
    plt.plot(xCoordinates,recCoordinates,label = "Recovered/Dead")
    plt.plot(xCoordinates,healthyCoordinates,label = "Healthy")
    plt.ylabel("Number of People")
    plt.xlabel("Number of Days")
    plt.legend()
    plt.show()
