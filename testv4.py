from collections import namedtuple
import tkinter as tk
from random import seed
from random import randint
import math

#opening all files
correctrep = open(r"correctorderpirep.txt", "r")
correctcp = open(r"correctorderpicp.txt", "r")
referencerep = open(r"unorderpirep.txt","r")
referencecp = open(r"unorderpicp.txt", "r")

#reading in file
input1 = correctrep.read().split()
input2 = correctcp.read().split()
input3 = referencerep.read().split()
input4 = referencecp.read().split()

#compile data into separate datasets for rep
count = 0
namesonlyrep = []
numsonlyrep = []
datasetrep = []
for str1 in input1:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        count += 1
        namesonlyrep.append(str1)
        if(count>1):
            datasetrep.append(numsonlyrep)
            numsonlyrep=[]
    elif(str1[0]==" "):
        pass
    elif(str1[len(str1)-1] == ":"):
        pass
    elif(str1[0]=="-"):
        numsonlyrep.append(None)
    else:
        numsonlyrep.append(str1)
datasetrep.append(numsonlyrep)

#compile data into separate datasets for cp
count = 0
namesonlycp = []
numsonlycp = []
datasetcp = []
for str1 in input2:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        count += 1
        namesonlycp.append(str1)
        if(count>1):
            datasetcp.append(numsonlycp)
            numsonlycp=[]
    elif(str1[0]==" "):
        pass
    elif(str1[len(str1)-1] == ":"):
        pass
    elif(str1[0]=="-"):
        numsonlycp.append(None)
    else:
        numsonlycp.append(str1)
datasetcp.append(numsonlycp)
        
#now you have names only, and numerical dataset for both rep and cp
#let's create the reference conversion chart for rep and cp

namesonlyrefrep =[]
for str1 in input3:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        namesonlyrefrep.append(str1)
namesonlyrefcp = []
for str1 in input4:
    if(str1==""):
        pass
    elif(str1[0].isalpha()):
        namesonlyrefcp.append(str1)

conversionchartrep = []
countx = -1
county = -1
for x in namesonlyrep:
    countx+=1
    county = -1
    for y in namesonlyrefrep:
        county += 1
        if(x==y):
            array=[]
            array.append(countx)
            array.append(county)
            conversionchartrep.append(array)
conversionchartcp = []
countx = -1
county = -1
for x in namesonlycp:
    countx+=1
    county = -1
    for y in namesonlyrefcp:
        county+=1
        if(x==y):
            array = []
            array.append(countx)
            array.append(county)
            conversionchartcp.append(array)
            
#let's create nodes based on the names only dataset

Node = namedtuple("Node",[ "name", "reppi", "cppi"])
nodes = []


for index in range(len(namesonlycp)):
    if(index<401):
        realname = ""
        name = namesonlyrep[index]
        for letter in range(len(name)):
            if(name[letter] == "-"):
                break
            else:
                realname += name[letter]
        n = Node(realname, datasetrep[index], datasetcp[index])
        nodes.append(n)
    elif(index < 403):
        realname = ""
        name = namesonlyrep[index]
        for letter in range(len(name)):
            if(name[letter] == "-"):
                break
            else:
                realname += name[letter]
        n = Node(realname, datasetrep[index], None)
        nodes.append(n)
        realname = ""
        name = namesonlycp[index]
        for letter in range(len(name)):
            if(name[letter] == "-"):
                break
            else:
                realname += name[letter]
        n = Node(realname, None, datasetcp[index])
        nodes.append(n)
    elif(index<412):
        realname = ""
        name = namesonlycp[index]
        for letter in range(len(name)):
            if(name[letter] == "-"):
                break
            else:
                realname += name[letter]
        n = Node(realname, None, datasetcp[index])
        nodes.append(n)

#now we have a list of 414 nodes: 401 of them have both cp+rep, 2 of them have only rep, 11 of them have only cp
#let's create an adjacency matrix to merge the data
print("what is the rep threshold?")
thresholdrep = int(input())
print("what is the cp threshold?")
thresholdcp = int(input())
adjacencymatrix = []
for a in range(414):
    currentmatrix = []
    for b in range(414):
        #if they are only cp
        if(a>404):
            if(b==401 or b==403):
                currentmatrix.append(None)
            else:
                n1 = nodes[a]
                n2 = nodes[b]
                if(b>402):
                    cp = n1.cppi[conversionchartcp[b-2][1]]
                elif(b==402):
                    cp=n1.cppi[conversionchartcp[b-1][1]]
                else:
                    cp=n1.cppi[conversionchartcp[b][1]]
                if(float(cp)>=thresholdcp):
                    currentmatrix.append(["c",cp])
                else:
                    currentmatrix.append(["n",0])
        #only cp values
        elif(b>404):
            if(a==401 or a==403):
                currentmatrix.append(None)
            else:
                n1 = nodes[a]
                n2 = nodes[b]
                if(b>402):
                    cp = n1.cppi[conversionchartcp[b-2][1]]
                elif(b==402):
                    cp=n1.cppi[conversionchartcp[b-1][1]]
                else:
                    cp=n1.cppi[conversionchartcp[b][1]]
                if(float(cp)>=thresholdcp):
                    currentmatrix.append(["c",cp])
                else:
                    currentmatrix.append(["n","0"])
        #normal nodes
        elif(a<401 and b<401):
            n1 = nodes[a]
            n2 = nodes[b]
            rep = n1.reppi[conversionchartrep[b][1]]
            cp = n1.cppi[conversionchartcp[b][1]]
            if(rep==None and cp==None):
                currentmatrix.append(None)
            elif(rep==None):
                if(float(cp)>=thresholdcp):
                    currentmatrix.append(["c",cp])
                else:
                    currentmatrix.append(["n",0])
            elif(cp==None):
                if(float(rep)>=thresholdrep):
                    currentmatrix.append(["r",rep])
                else:
                    currentmatrix.append(["n",0])
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
        #only rep/cp from 401-404
        else:
            #only rep
            if(a==401 or a==403):
                if(b==402 or b==404):
                    currentmatrix.append(None)
                else:
                    n1 = nodes[a]
                    n2 = nodes[b]
                    if(b==401):
                        rep=n1.reppi[conversionchartrep[401][1]]
                    elif(b==403):
                        rep=n1.reppi[conversionchartrep[402][1]]
                    else:
                        rep=n1.reppi[conversionchartrep[b][1]]
                    if(float(rep)>=thresholdrep):
                        currentmatrix.append(["r",rep])
                    else:
                        currentmatrix.append(["n","0"])
            #only rep
            elif(b==401 or b==403):
                if(a==402 or a==404):
                    currentmatrix.append(None)
                else:
                    n1=nodes[a]
                    n2=nodes[b]
                    if(b==401):
                        rep=n1.reppi[conversionchartrep[401][1]]
                    elif(b==403):
                        rep=n1.reppi[conversionchartrep[402][1]]
                    else:
                        rep=n1.reppi[conversionchartrep[b][1]]
                    if(float(rep)>=thresholdrep):
                        currentmatrix.append(["r",rep])
                    else:
                        currentmatrix.append(["n","0"])
            #only cp
            elif(a==402 or a==404):
                if(b==401 or b==403):
                    currentmatrix.append(None)
                else:
                    n1 = nodes[a]
                    n2 = nodes[b]
                    if(b==402):
                        cp = n1.cppi[conversionchartcp[401][1]]
                    elif(b==404):
                        cp = n1.cppi[conversionchartcp[402][1]]
                    else:
                        cp = n1.cppi[conversionchartcp[b][1]]
                    if(float(cp)>=thresholdcp):
                        currentmatrix.append(["c",cp])
                    else:
                        currentmatrix.append(["n","0"])
            #only cp
            else:
                n1 = nodes[a]
                n2 = nodes[b]
                if(b==402):
                    cp = n1.cppi[conversionchartcp[401][1]]
                elif(b==404):
                    cp = n1.cppi[conversionchartcp[402][1]]
                else:
                    cp = n1.cppi[conversionchartcp[b][1]]
                if(float(cp)>=thresholdcp):
                    currentmatrix.append(["c",cp])
                else:
                    currentmatrix.append(["n","0"])
            
    adjacencymatrix.append(currentmatrix)
print("do you want edges? (y/n)")
wantedges=input()
print("how many nodes do you want to display (max 414)")
nodestodisplay=int(input())
    
    

#initialize our root and tkinter

class Example(tk.Frame):
    
    #main method: first initialize tkinter, put all non-method code
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self, width=1600, height=900, background="white")
        self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,1000,1000))

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        seed(1)

        #archived for now, but this method creates a database of all paths for all nodes
        
        #databaseofpaths = []
        #for a in range(414):
         #   print(a/414)
          #  patharray=[]
           # currentpath=[nodes[a]]
            #patharray=self.recursive(0,a,currentpath,patharray,adjacencymatrix,nodes)
            #databaseofpaths.append(patharray)

        #self.printPaths(databaseofpaths)
        
        #draw all circles by cycling through adjacency matrix and creating nodes in the order of their connection
        #randomize if no connection, otherwise, use our edge length formula to place the circle
        
        circles = []
        creatednode = []
        
        for a in range(nodestodisplay):
            circles.append(0)
            
        for a in range(nodestodisplay):
            n = nodes[a]
            neighbors=self.getDrawnNeighbors(a,adjacencymatrix)
            if(creatednode.count(n)==0):
                for b in range(a):
                    n2=nodes[b]
                    if(adjacencymatrix[a][b]!=None and adjacencymatrix[a][b][0]!="n" and creatednode.count(n2)==1):
                        if(creatednode.count(n)==0):
                            print(a, n.name, "created connected")
                            circlecenterx=self.canvas.coords(circles[b])[0]+8
                            circlecentery=self.canvas.coords(circles[b])[1]+8
                            length = int(50-50*(float(adjacencymatrix[a][b][1])-thresholdrep)/(100-thresholdrep)+20)
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
                            print("for", a, ":",b, "needs to cooperate with", neighbors[0])
                            #triangle case
                            if(adjacencymatrix[neighbors[0]][b]!=None and adjacencymatrix[neighbors[0]][b][0]!="n"):
                                possiblepoints1=self.getPossiblePoints(circles, neighbors[0],a, adjacencymatrix)
                                possiblepoints2=self.getPossiblePoints(circles, b,a, adjacencymatrix)
                                closestpairs=self.optimizePoints(possiblepoints1,possiblepoints2)
                                print(closestpairs[0],closestpairs[1])
                                print(closestpairs[2], closestpairs[3])
                                self.canvas.delete(circles[a])
                                label=n.name
                                newx=(closestpairs[0]+closestpairs[2])/2
                                newy=(closestpairs[1]+closestpairs[3])/2
                                self.createNode(newx, newy, 8, label, circles, a)
                            #line case
                            else:
                                #v case, we will move one of the nodes!
                                if(len(self.getDrawnNeighbors(neighbors[0],adjacencymatrix))==0 and len(self.getDrawnNeighbors(b, adjacencymatrix))==0):
                                    print("made it in here!")
                                    self.canvas.delete(circles[b])
                                    circlecenterx=self.canvas.coords(circles[a])[0]+8
                                    circlecentery=self.canvas.coords(circles[a])[1]+8
                                    length = int(50-50*(float(adjacencymatrix[a][b][1])-thresholdrep)/(100-thresholdrep)+20)
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
                                else:
                                    print("ok, looks like we have to move a whole cluster :(")
                                    listofnodestomove=self.getConnections(b,a,[b])
                                    print(n2.name, "is connected to", listofnodestomove)
                                    circlecenterx=self.canvas.coords(circles[a])[0]+8
                                    circlecentery=self.canvas.coords(circles[a])[1]+8
                                    length = int(50-50*(float(adjacencymatrix[a][b][1])-thresholdrep)/(100-thresholdrep)+20)
                                    label = n2.name
                                    deltax=randint(0,length)
                                    deltay = math.sqrt(length*length-deltax*deltax)
                                    oldcenterx=self.canvas.coords(circles[b])[0]+8
                                    oldcentery=self.canvas.coords(circles[b])[1]+8
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
                                    print(a, "is", circlecenterx,circlecentery)
                                    print(b, "is", oldcenterx, oldcentery)
                                    print(b, "will be", newx,newy)
                                    changex=newx-oldcenterx
                                    changey=newy-oldcentery
                                    for c in listofnodestomove:
                                        oldcenterx=self.canvas.coords(circles[c])[0]+8
                                        oldcentery=self.canvas.coords(circles[c])[1]+8
                                        label = nodes[c].name
                                        self.canvas.delete(circles[c])
                                        self.createNode(oldcenterx+changex,oldcentery+changey, 8, label, circles, c) 
                                    
                print(a, "neighbors:", len(neighbors))            
                if(creatednode.count(n)==0):
                    print(a,n.name,"created randomly")
                    label = n.name
                    num=randint(8,1592)
                    num2=randint(8,892)
                    self.createNode(num, num2, 8, label, circles, a)
                    creatednode.append(n)


        #initialize edge array
        
        countl=0
        drewline=[]

        for a in range(nodestodisplay):
            array=[]
            for b in range(nodestodisplay):
                array.append(False)
            drewline.append(array)

        #cycle through adjacency matrix and draw edges if needed also change color based on rcb


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
                        self.connectNodes(a,b,circles[a],circles[b], color)

        for circle in circles:
            coords=self.canvas.coords(circle)
            tags1=self.canvas.gettags(circle)
            self.canvas.create_oval(coords[0], coords[1], coords[2], coords[3],fill='green', width=0, tags=tags1)

            
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




    #recursive function for to find all paths for all nodes
    def recursive(self,prev, start, currentpath, patharray, adjacencymatrix, nodes):
        #cycle through adjacency matrix and look for "neighbors" of start. add them to current path as long as current path doesn't already contain it
        for a in range(414):
            if(a!=start and adjacencymatrix[start][a]!=None and (adjacencymatrix[start][a][0]=="r" or adjacencymatrix[start][a][0]=="c" or adjacencymatrix[start][a][0]=="b")):
                if(currentpath.count(nodes[a])==0):
                    temp = currentpath.copy()
                    temp.append(nodes[a])
                    patharray.append(temp)
                    patharray=self.recursive(start, a, temp, patharray, adjacencymatrix, nodes)
        return patharray

    #just a print method to see the database of paths
    def printPaths(self, databaseofpaths):
        for paths in databaseofpaths:
            if(len(paths)==0):
                pass
            else:
                for path in paths:
                    arraynames=[]
                    for node in path:
                        arraynames.append(node.name)
                    print(arraynames)
                print("")
    
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
        o = self.canvas.create_oval(centerx-radius, centery-radius, centerx+radius, centery+radius, fill = "green", width = 0, tags = label)
        circles[index]=o

    #given 2 circles, connect them with a line in the color given
    def connectNodes(self,a,b,circle1,circle2, color):
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

    def getPossiblePoints(self,circles, stationary, moving, adjacencymatrix):
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

    
    def getConnections(self,a,current,listOfConnections):
        neighbors=self.getCurrentNeighbors(a,current,adjacencymatrix)
        for neighbor in neighbors:
            if(listOfConnections.count(neighbor)==0):
                listOfConnections.append(neighbor)
                listofConnections=self.getConnections(neighbor,current, listOfConnections)
        return listOfConnections
    
    def getDrawnNeighbors(self, a, adjacencymatrix):
        neighbors=[]
        for b in range(a):
            if(adjacencymatrix[a][b]!=None and adjacencymatrix[a][b][0]!="n"):
                neighbors.append(b)
        return neighbors


    def getCurrentNeighbors(self, a, current, adjacencymatrix):
        neighbors=[]
        for b in range(current):
            if(adjacencymatrix[a][b]!=None and adjacencymatrix[a][b][0]!="n" and b!=a):
                neighbors.append(b)
        return neighbors

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
