#! /usr/bin/env python3
from collections import namedtuple
import tkinter as tk
from random import seed
from random import randint
import math

#opening all files
cruciCp = open(r"CruciCpPi.txt", "r")
cressCp = open(r"CressCpPi.txt","r")
allRep = open(r"AllRepPi.txt","r")

#opening all name files
cruciCpFasta = open(r"CruciCpFasta.fasta","r")
cruciRepFasta = open(r"CruciRepFasta.fasta","r")
cressCpFasta = open(r"CressCpFasta.fasta", "r")
cressRepFasta = open(r"CressRepFasta.fasta", "r")
p4mpRepFasta = open(r"P4mpRepFasta.fasta", "r")
pCPaRepFasta = open(r"PCPaRepFasta.fasta", "r")
pPaPh2likeRepFasta = open(r"PPaPh2likeRepFasta.fasta", "r")
pPulchraRepFasta = open(r"PpulchraRepFasta.fasta", "r")


#reading in file
input1 = cruciCp.read().split()
input2 = cressCp.read().split()
input3 = allRep.read().split()




#first we need to compile all the names and assign each name a value
namesonlyall = []
count = 0
totalCount=0
for str1 in input1:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        name=""
        for letter in range(len(str1)):
            if(str1[letter]=="-" and str1[letter+1]=="_"):
                break
            else:
                name+=str1[letter]
        namesonlyall.append(name)
        count=count+1
    else:
        pass

for str1 in input2:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        name=""
        for letter in range(len(str1)):
            if(str1[letter]=="-" and str1[letter+1]=="_"):
                break
            else:
                name+=str1[letter]
        namesonlyall.append(name)
        count=count+1
    else:
        pass

duplicates = 0
for str1 in input3:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        name=""
        for letter in range(len(str1)):
            if(str1[letter]=="-" and str1[letter+1]=="_"):
                break
            else:
                name+=str1[letter]
        if name in namesonlyall:
            duplicates=duplicates+1
            pass
        else:
            namesonlyall.append(name)
            count=count+1
    else:
        pass

#we have finished compiling all the non-duplicate names yay!
#find how the order of the cruci compares to our master list
orderCruciCp=[]
for str1 in input1:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        name=""
        for letter in range(len(str1)):
            if(str1[letter]=="-" and str1[letter+1]=="_"):
                break
            else:
                name+=str1[letter]
        orderCruciCp.append(namesonlyall.index(name))
    else:
        pass


orderCressCp=[]
for str1 in input2:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        name=""
        for letter in range(len(str1)):
            if(str1[letter]=="-" and str1[letter+1]=="_"):
                break
            else:
                name+=str1[letter]
        orderCressCp.append(namesonlyall.index(name))
    else:
        pass

orderAllRep=[]
for str1 in input3:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        name=""
        for letter in range(len(str1)):
            if(str1[letter]=="-" and str1[letter+1]=="_"):
                break
            else:
                name+=str1[letter]
        orderAllRep.append(namesonlyall.index(name))
    else:
        pass

#compile data into separate datasets for rep
countNames = 0
countNumber = 0;
numsonlycp = [None]*len(namesonlyall)
datasetcp = [None]*len(namesonlyall)
count = 0
firstIndex=0
for str1 in input1:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        countNames += 1

        name=""
        for letter in range(len(str1)):
            if(str1[letter]=="-" and str1[letter+1]=="_"):
                break
            else:
                name+=str1[letter]

        firstIndex = namesonlyall.index(name)
        if(countNames>1):
            datasetcp[firstIndex-1]=numsonlycp
            numsonlycp=[None]*len(namesonlyall)
            countNumber = 0
    elif(str1[0]==" "):
        pass
    elif(str1[len(str1)-1] == ":"):
        pass
    elif(str1[0]=="-"):
        pass
    else:
        numsonlycp[orderCruciCp[countNumber]]=str1
        countNumber=countNumber+1
        
datasetcp[firstIndex]=numsonlycp


countNames = 0
countNumber = 0;
numsonlycp = [None]*len(namesonlyall)
count = 0
firstIndex=0
for str1 in input2:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        countNames += 1

        name=""
        for letter in range(len(str1)):
            if(str1[letter]=="-" and str1[letter+1]=="_"):
                break
            else:
                name+=str1[letter]

        if(countNames>1):
            datasetcp[firstIndex]=numsonlycp
            numsonlycp=[None]*len(namesonlyall)
            countNumber = 0
        firstIndex = namesonlyall.index(name)

    elif(str1[0]==" "):
        pass
    elif(str1[len(str1)-1] == ":"):
        pass
    elif(str1[0]=="-"):
        pass
    else:
        numsonlycp[orderCressCp[countNumber]]=str1
        countNumber=countNumber+1
        
datasetcp[firstIndex]=numsonlycp


print(len(namesonlyall))

#compile data into separate datasets for rep
countNames = 0
countNumber = 0;
numsonlyrep = [None]*len(namesonlyall)
datasetrep = [None]*len(namesonlyall)
count = 0
firstIndex=0
for str1 in input3:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        countNames += 1

        name=""
        for letter in range(len(str1)):
            if(str1[letter]=="-" and str1[letter+1]=="_"):
                break
            else:
                name+=str1[letter]
        if(countNames>1):
            datasetrep[firstIndex]=numsonlyrep
            numsonlyrep=[None]*len(namesonlyall)
            countNumber = 0
        firstIndex = namesonlyall.index(name)
    elif(str1[0]==" "):
        pass
    elif(str1[len(str1)-1] == ":"):
        pass
    elif(str1[0]=="-"):
        pass
    else:
        numsonlyrep[orderAllRep[countNumber]]=str1
        countNumber=countNumber+1
        
datasetrep[firstIndex]=numsonlyrep
print(datasetrep[84])

# #now you have names only, and numerical dataset for both rep and cp
# #let's get the names in unvelied and new so we can color the nodes later on
input4 = cruciRepFasta.read().split()

cruciNames=[]

for str1 in input4:
    if(str1==""):
        pass
    elif(str1[0]==">"):
        name=""
        for letter in range(len(str1)):
            if(letter!=0):
                if(str1[letter]=="-" and str1[letter+1]=="_"):
                    break
                else:
                    name+=str1[letter]
        cruciNames.append(name)
    else:
        pass

input5 = cruciCpFasta.read().split()
    
for str1 in input5:
    if(str1==""):
        pass
    elif(str1[0]==">"):
        name=""
        for letter in range(len(str1)):
            if(letter!=0):
                if(str1[letter]=="-" and str1[letter+1]=="_"):
                    break
                else:
                    name+=str1[letter]
        if name in cruciNames:
            pass
        else:
            cruciNames.append(name)
    else:
        pass

input6 = cressRepFasta.read().split()

cressNames=[]

for str1 in input6:
    if(str1==""):
        pass
    elif(str1[0]==">"):
        name=""
        for letter in range(len(str1)):
            if(letter!=0):
                if(str1[letter]=="-" and str1[letter+1]=="_"):
                    break
                else:
                    name+=str1[letter]
        cressNames.append(name)
    else:
        pass

input7 = cressCpFasta.read().split()
    
for str1 in input7:
    if(str1==""):
        pass
    elif(str1[0]==">"):
        name=""
        for letter in range(len(str1)):
            if(letter!=0):
                if(str1[letter]=="-" and str1[letter+1]=="_"):
                    break
                else:
                    name+=str1[letter]
        if name in cressNames:
            pass
        else:
            cressNames.append(name)
    else:
        pass


input8 = p4mpRepFasta.read().split()

p4mpNames=[]

for str1 in input8:
    if(str1==""):
        pass
    elif(str1[0]==">"):
        name=""
        for letter in range(len(str1)):
            if(letter!=0):
                if(str1[letter]=="-" and str1[letter+1]=="_"):
                    break
                else:
                    name+=str1[letter]
        p4mpNames.append(name)
    else:
        pass


input9 = pCPaRepFasta.read().split()

pcpaNames=[]

for str1 in input9:
    if(str1==""):
        pass
    elif(str1[0]==">"):
        name=""
        for letter in range(len(str1)):
            if(letter!=0):
                if(str1[letter]=="-" and str1[letter+1]=="_"):
                    break
                else:
                    name+=str1[letter]
        pcpaNames.append(name)
    else:
        pass



input10 = pPaPh2likeRepFasta.read().split()

ppaph2Names=[]

for str1 in input10:
    if(str1==""):
        pass
    elif(str1[0]==">"):
        name=""
        for letter in range(len(str1)):
            if(letter!=0):
                if(str1[letter]=="-" and str1[letter+1]=="_"):
                    break
                else:
                    name+=str1[letter]
        ppaph2Names.append(name)
    else:
        pass



input11 = pPulchraRepFasta.read().split()

ppulchraNames=[]

for str1 in input11:
    if(str1==""):
        pass
    elif(str1[0]==">"):
        name=""
        for letter in range(len(str1)):
            if(letter!=0):
                if(str1[letter]=="-" and str1[letter+1]=="_"):
                    break
                else:
                    name+=str1[letter]
        ppulchraNames.append(name)
    else:
        pass


#let's create nodes based on the names only database

Node = namedtuple("Node",[ "name", "reppi", "cppi"])
nodes = []

for index in range(len(namesonlyall)):
    n = Node(namesonlyall[index], datasetrep[index], datasetcp[index])
    nodes.append(n)

print("do you want edges? (y/n)")
wantedges=input()
print("how many nodes do you want to display (max 1749)")
nodestodisplay=int(input())
             

#initialize our root and tkinter

class Example(tk.Frame):
    
    #main method: first initialize tkinter, put all non-method code
    def __init__(self, root):
        #main frame with canvas and scroll bars
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self, width=1600, height=900, background="white")
        self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

        #small subframe that carries all our sliders and the go button
        self.frame = tk.Frame(self)
        self.textrep=tk.Label(self.frame, text="rep \nthreshold")
        self.sliderrep = tk.Scale(self.frame, from_=0, to=100,orient="vertical", length=200)
        self.textcp=tk.Label(self.frame, text="cp \nthreshold")
        self.slidercp = tk.Scale(self.frame, from_=0, to=100, orient="vertical", length=200)
        self.textlength=tk.Label(self.frame, text="edge length \nrange")
        self.sliderlength = tk.Scale(self.frame, from_=20, to=200, orient="vertical", length=200)
        self.buttongo=tk.Button(self.frame, text="go!", command=lambda : self.recreateGraph())

        #configure the canvas scrolling
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,1000,1000))

        #set up the scrollbars and canvas in the main gridframe
        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=2, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.frame.grid(row=0, column=1)

        #set up the sliders in the sub gridframe
        self.textrep.grid(row=0, column=0)
        self.sliderrep.grid(row=1, column=0)
        self.textcp.grid(row=2, column=0)
        self.slidercp.grid(row=3, column=0)
        self.textlength.grid(row=4, column=0)
        self.sliderlength.grid(row=5, column=0)
        self.buttongo.grid(row=6, column=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        seed(1)

            
        #key bindings for mouse and keys
        # This is what enables using the mouse:
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)
        self.canvas.bind("<Button-3>", self.getData)
        #linux scroll
        self.canvas.bind("<Button-4>", self.zoomerP)
        self.canvas.bind("<Button-5>", self.zoomerM)
        #windows scroll
        self.canvas.bind("<MouseWheel>",self.zoomer)

    #this method activates when we press the go button, it re draws the graph given the new slider values
    def recreateGraph(self):
        thresholdrep=(self.sliderrep.get())
        thresholdcp=self.slidercp.get()
        lengthrange = self.sliderlength.get()
        self.canvas.delete("all")
        adjacencymatrix=self.getAdjacencyMatrix(thresholdrep, thresholdcp)
        self.createGraph(adjacencymatrix, thresholdrep, lengthrange)

    
    #move
    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    #windows zoom
    def zoomer(self,event):
        if (event.delta > 0):
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif (event.delta < 0):
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    #linux zoom
    def zoomerP(self,event):
        self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
    def zoomerM(self,event):
        self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    #draws a circle based on radius and center, gives a pre-set label
        
    def createNode(self, centerx, centery, radius,label, circles, index):
        color="dark red"
        if(label in cruciNames):
            color="coral"
        elif(label in cressNames):
            color="green yellow"
        elif(label in p4mpNames):
            color="plum1"
        elif(label in pcpaNames):
            color="gold"
        elif(label in ppaph2Names):
            color="violet red"
        elif(label in ppulchraNames):
            color="hot pink"
            
        o = self.canvas.create_oval(centerx-radius, centery-radius, centerx+radius, centery+radius, fill = color, width = 1, tags = label)
        circles[index]=o

    #given 2 circles, connect them with a line in the color given
    def connectNodes(self,a,b,circle1,circle2, color, adjacencymatrix):
        node1 = self.canvas.gettags(circle1)[0]
        node2 = self.canvas.gettags(circle2)[0]
        if(node1==node2):
            return
        else:
            circle1points = self.canvas.coords(circle1)
            circle2points = self.canvas.coords(circle2)
            center1x = circle1points[0]+8
            center1y = circle1points[1]+8
            center2x = circle2points[0]+8
            center2y = circle2points[1]+8
            l = self.canvas.create_line(center1x, center1y, center2x, center2y, width = 0.5, fill=color)
            deltay = center2y-center1y
            deltax = center2x-center1x
            self.canvas.itemconfig(l, tags="pi: "+ str(adjacencymatrix[a][b][1]) + "\n" + node1 + "        " + node2)


    #right click to get pop up box w info
    def getData(self,event):
        circle = event.widget.find_withtag("current")
        tags_text = ', '.join(self.canvas.gettags(circle))
        top = tk.Toplevel()
        top.title('Datapoint')
        top.geometry("500x100")
        tk.Message(top, text=tags_text, width=500).pack()
        top.after(5000,top.destroy)

    #given a stationary circle, generate all possible points around that circle's centerpoint with the correct radius 
    def getPossiblePoints(self,circles, stationary, moving, adjacencymatrix, thresholdrep):
        hypotenuse = int(50-50*(float(adjacencymatrix[stationary][moving][1])-thresholdrep)/(100-thresholdrep)+20)
        stationaryx=self.canvas.coords(circles[stationary])[0]+8
        stationaryy=self.canvas.coords(circles[stationary])[1]+8
        possiblepoints=[]
        for a in range(120):
            degrees = 3*a
            radians=degrees*math.pi/180
            deltax=math.cos(radians)*hypotenuse
            deltay=math.sin(radians)*hypotenuse
            coords=[]
            coords.append(stationaryx+deltax)
            coords.append(stationaryy+deltay)
            possiblepoints.append(coords)
        return possiblepoints

    #given two sets of possible points, return the pair that is the closest to eachother
    def optimizePoints(self, possiblepoints1, possiblepoints2):
        diff = 1000000000000
        coords=[]
        for point1 in possiblepoints1:
            for point2 in possiblepoints2:
                tempdiff = math.fabs(point1[0]-point2[0])+math.fabs(point1[1]-point2[1])
                if(tempdiff < diff):
                    diff=tempdiff
                    coords=[point1[0],point1[1],point2[0],point2[1]]
        return coords

    #a recursive function that returns a cumulative list of all nodes directly/indirectly connected and drawn to node a
    def getConnections(self,a,current,listOfConnections, adjacencymatrix):
        neighbors=self.getCurrentNeighbors(a,current,adjacencymatrix)
        for neighbor in neighbors:
            if(listOfConnections.count(neighbor)==0):
                listOfConnections.append(neighbor)
                listofConnections=self.getConnections(neighbor,current, listOfConnections, adjacencymatrix)
        return listOfConnections

    #get all direct neighbors that have already been drawn at the time a is being drawn
    def getDrawnNeighbors(self, a, adjacencymatrix):
        neighbors=[]
        for b in range(a):
            if(adjacencymatrix[a][b]!=None and adjacencymatrix[a][b][0]!="n"):
                neighbors.append(b)
        return neighbors

    #get all direct neighbors that have already been drawn at the time current is being drawn
    def getCurrentNeighbors(self, a, current, adjacencymatrix):
        neighbors=[]
        for b in range(current):
            if(adjacencymatrix[a][b]!=None and adjacencymatrix[a][b][0]!="n" and b!=a):
                neighbors.append(b)
        return neighbors

    #given two thresholds, generate and return an adjacencymatrix 
    def getAdjacencyMatrix(self, thresholdrep, thresholdcp):
        adjacencymatrix = []
        for a in range(len(nodes)):
            currentmatrix = []
            for b in range(len(nodes)):
                #normal nodes
                n1 = nodes[a]
                n2 = nodes[b]
                if(n1.reppi==None):
                    rep=n1.reppi
                else:
                    rep = n1.reppi[b]
                if(n1.cppi==None):
                    cp = n1.cppi
                else:
                    cp = n1.cppi[b]
                if(rep==None and cp==None):
                    currentmatrix.append(["n","0"])
                elif(rep==None):
                    if(float(cp)>=thresholdcp):
                        currentmatrix.append(["c",cp])
                    else:
                        currentmatrix.append(["n","0"])
                elif(cp==None):
                    if(float(rep)>=thresholdrep):
                        currentmatrix.append(["r",rep])
                    else:
                        currentmatrix.append(["n","0"])
                elif(float(rep)>=thresholdrep and float(cp)>=thresholdcp):
                    nums = (float(rep)+float(cp))/2
                    avg = str(nums)
                    currentmatrix.append(["b",avg])
                elif(float(rep)>=thresholdrep):
                    currentmatrix.append(["r",rep])
                elif(float(cp)>=thresholdcp):
                    currentmatrix.append(["c",cp])
                else:
                    currentmatrix.append(["n","0"])
            adjacencymatrix.append(currentmatrix)
        return adjacencymatrix

    #given an adjacency matrix and length parameters, generate a graph
    def createGraph(self, adjacencymatrix, thresholdrep, lengthrange):
        numbererrors = 0
        runningerror = 0
        circles = []
        creatednode = []

        #initialize the circles array
        for a in range(nodestodisplay):
            circles.append(0)

        #cycle through all nodes
        for a in range(nodestodisplay):
            n = nodes[a]
            neighbors=self.getDrawnNeighbors(a,adjacencymatrix)
            #if the circle for the node has not been drawn yet
            if(creatednode.count(n)==0):
                #cycle through all nodes drawn so far
                for b in range(a):
                    n2=nodes[b]
                    #if the two nodes at a and b have a pi val over the threshold, and b has been drawn already
                    if(adjacencymatrix[a][b]!=None and adjacencymatrix[a][b][0]!="n" and creatednode.count(n2)==1):
                        #if node a has not been drawn yet, draw it at a random point at the correct length away from b, and add node a to the created node array
                        if(creatednode.count(n)==0):
                            print(a, n.name, "created connected")
                            circlecenterx=self.canvas.coords(circles[b])[0]+8
                            circlecentery=self.canvas.coords(circles[b])[1]+8
                            length = int(lengthrange-lengthrange*(float(adjacencymatrix[a][b][1])-thresholdrep)/(100-thresholdrep)+20)
                            label = n.name
                            deltax=randint(0,length)
                            deltay = math.sqrt(length*length-deltax*deltax)
                            randcorner = randint(1,4)
                            if(randcorner==1):
                                self.createNode(circlecenterx+deltax, circlecentery-deltay, 8, label, circles, a)
                            elif(randcorner==2):
                                self.createNode(circlecenterx-deltax, circlecentery-deltay, 8, label, circles, a)
                            elif(randcorner==3):
                                self.createNode(circlecenterx-deltax, circlecentery+deltay, 8, label, circles, a)
                            else:
                                self.createNode(circlecenterx+deltax, circlecentery+deltay, 8, label, circles, a)
                            creatednode.append(n)
                        else:
                            #in a triangle case, get the possible points around the first connection and the current connection, and find the closest pair of points
                            #then redraw the node at that pair of points 
                            if(adjacencymatrix[neighbors[0]][b]!=None and adjacencymatrix[neighbors[0]][b][0]!="n"):
                                possiblepoints1=self.getPossiblePoints(circles, neighbors[0],a, adjacencymatrix, thresholdrep)
                                possiblepoints2=self.getPossiblePoints(circles, b,a, adjacencymatrix, thresholdrep)
                                closestpairs=self.optimizePoints(possiblepoints1,possiblepoints2)
                                self.canvas.delete(circles[a])
                                label=n.name
                                newx=(closestpairs[0]+closestpairs[2])/2
                                newy=(closestpairs[1]+closestpairs[3])/2
                                differencex = (closestpairs[2]-closestpairs[0])
                                differencey = closestpairs[1]-closestpairs[3]
                                realdiff = math.sqrt(math.pow(differencex, 2)+math.pow(differencey, 2))
                                print(realdiff)
                                numbererrors += 1
                                runningerror += realdiff
                                self.createNode(newx, newy, 8, label, circles, a)
                            else:
                                #v case, we will move one of the nodes!
                                if(len(self.getCurrentNeighbors(neighbors[0],a,adjacencymatrix))==0 and len(self.getCurrentNeighbors(b,a, adjacencymatrix))==0):
                                    self.canvas.delete(circles[b])
                                    circlecenterx=self.canvas.coords(circles[a])[0]+8
                                    circlecentery=self.canvas.coords(circles[a])[1]+8
                                    length = int(lengthrange-lengthrange*(float(adjacencymatrix[a][b][1])-thresholdrep)/(100-thresholdrep)+20)
                                    label = n2.name
                                    deltax=randint(0,length)
                                    deltay = math.sqrt(length*length-deltax*deltax)
                                    randcorner = randint(1,4)
                                    if(randcorner==1):
                                        self.createNode(circlecenterx+deltax, circlecentery-deltay, 8, label, circles, b)
                                    elif(randcorner==2):
                                        self.createNode(circlecenterx-deltax, circlecentery-deltay, 8, label, circles, b)
                                    elif(randcorner==3):
                                        self.createNode(circlecenterx-deltax, circlecentery+deltay, 8, label, circles, b)
                                    else:
                                        self.createNode(circlecenterx+deltax, circlecentery+deltay, 8, label, circles, b)
                                #this means we have to move a whole cluster! 
                                else:
                                    #get a list of all the nodes connected to the node we have to move
                                    listofnodestomove=self.getConnections(b,a,[b], adjacencymatrix)
                                    circlecenterx=self.canvas.coords(circles[a])[0]+8
                                    circlecentery=self.canvas.coords(circles[a])[1]+8
                                    length = int(lengthrange-lengthrange*(float(adjacencymatrix[a][b][1])-thresholdrep)/(100-thresholdrep)+20)
                                    label = n2.name
                                    deltax=randint(0,length)
                                    deltay = math.sqrt(length*length-deltax*deltax)
                                    oldcenterx=self.canvas.coords(circles[b])[0]+8
                                    oldcentery=self.canvas.coords(circles[b])[1]+8
                                    #we want to move our cluster to the same relative quadrant as it was before
                                    if(circlecenterx-oldcenterx>0):
                                        newx=circlecenterx-deltax
                                        if(circlecentery-oldcentery>0):
                                            newy=circlecentery-deltay
                                        else:
                                            newy=circlecentery+deltay
                                    else:
                                        newx=circlecenterx+deltax
                                        if(circlecentery-oldcentery>0):
                                            newy=circlecentery-deltay
                                        else:
                                            newy=circlecentery+deltay
                                    changex=newx-oldcenterx
                                    changey=newy-oldcentery
                                    #move all of the nodes in the cluster by the moving factor
                                    for c in listofnodestomove:
                                        oldcenterx=self.canvas.coords(circles[c])[0]+8
                                        oldcentery=self.canvas.coords(circles[c])[1]+8
                                        label = nodes[c].name
                                        self.canvas.delete(circles[c])
                                        self.createNode(oldcenterx+changex,oldcentery+changey, 8, label, circles, c) 

                #if no original created connections, randomly generate a point and draw a circle there
                if(creatednode.count(n)==0):
                    print(a,n.name,"created randomly")
                    label = n.name
                    num=randint(8,1592)
                    num2=randint(8,892)
                    self.createNode(num, num2, 8, label, circles, a)
                    creatednode.append(n)


        print(runningerror/numbererrors)

        #cycle through adjacency matrix and draw edges if needed also change color based on rep only, cp only, or both

        if(wantedges=="y"):
            for a in range(nodestodisplay):
                for b in range(nodestodisplay):
                    if(adjacencymatrix[a][b]==None):
                        pass
                    elif(adjacencymatrix[a][b][0]=="n"):
                        pass
                    else:
                        if(adjacencymatrix[a][b][0]=="r"):
                            color='red'
                        elif(adjacencymatrix[a][b][0]=="c"):
                            color='DeepSkyBlue2'
                        else:
                            color='purple'
                        self.connectNodes(a,b,circles[a],circles[b], color, adjacencymatrix)

        #redraw circles on top of edges
        for circle in circles:
            coords=self.canvas.coords(circle)
            tags1=self.canvas.gettags(circle)
            color=self.canvas.itemcget(circle,'fill')
            self.canvas.create_oval(coords[0], coords[1], coords[2], coords[3],fill=color, width=1, tags=tags1)


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()

