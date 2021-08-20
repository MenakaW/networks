#! /usr/bin/env python3
import tkinter as tk
from random import seed
from random import randint
import math
from collections import namedtuple

file1 = open("CorrectCPS.txt","r")
file2 = open("orderedreps451.txt", "r")
s=file1.read()
t=file2.read()

    
print("do you want edges? (y/n)")
wantedges=input()
print("how many nodes do you want to display (max 462)")
nodestodisplay=int(input())
    
    

#initialize our root and tkinter

class Example(tk.Frame):

    #main method: first initialize tkinter, put all non-method code
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self, width=1600, height=900, background="white")
        self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

        self.frame = tk.Frame(self)
        self.textrep=tk.Label(self.frame, text="rep \nthreshold")
        self.sliderrep = tk.Scale(self.frame, from_=0, to=100,orient="vertical", length=200)
        self.textcp=tk.Label(self.frame, text="cp \nthreshold")
        self.slidercp = tk.Scale(self.frame, from_=0, to=100, orient="vertical", length=200)
        self.textlength=tk.Label(self.frame, text="edge length \nrange")
        self.sliderlength = tk.Scale(self.frame, from_=20, to=200, orient="vertical", length=200)
        self.buttongo=tk.Button(self.frame, text="go!", command=lambda : self.recreateGraph())
        self.percent = tk.Label(self.frame, text = "0%")
        
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,1000,1000))

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=2, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.frame.grid(row=0, column=1)
        
        self.percent.grid(row = 0, column = 0)
        self.textrep.grid(row=1, column=0)
        self.sliderrep.grid(row=2, column=0)
        self.textcp.grid(row=3, column=0)
        self.slidercp.grid(row=4, column=0)
        self.textlength.grid(row=5, column=0)
        self.sliderlength.grid(row=6, column=0)
        self.buttongo.grid(row=7, column=0)

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
        
        
        tvaluereps = 0
        tvaluecps = 0
        length = 0


    def recreateGraph(self):
        tvaluereps=(self.sliderrep.get())
        tvaluecps=self.slidercp.get()
        lengthrange = self.sliderlength.get()
        self.canvas.delete("all")
        finalmatrix=self.getMatrix(s,t,tvaluereps, tvaluecps)
        amatrix = finalmatrix[0]
        self.createGraph(amatrix, tvaluereps, lengthrange,finalmatrix, tvaluecps)

    def createGraph(self, amatrix, tvaluereps, lengthrange, finalmatrix, tvaluecps):

        Node = namedtuple("Node",["name", "reppi", "cppi"])
        nodes = []

        for i in range(462):
            n = Node(finalmatrix[1][i], finalmatrix[2][i], finalmatrix[3][i])
            nodes.append(n)
        
        circles = []
        creatednode = []

        for a in range(nodestodisplay):
            circles.append(0)

        for a in range(nodestodisplay):
            n = nodes[a]
            neighbors=self.getDrawnNeighbors(a,amatrix)
            if(creatednode.count(n)==0):
                for b in range(a):
                    n2=nodes[b]
                    if(amatrix[a][b][1]!=0.0 and amatrix[a][b][0]!="bb" and amatrix[a][b][1]!=0 and creatednode.count(n2)==1):
                        if(creatednode.count(n)==0):
                            print(a, n.name, "created connected")
                            circlecenterx=self.canvas.coords(circles[b])[0]+8
                            circlecentery=self.canvas.coords(circles[b])[1]+8
                            length = int(lengthrange-lengthrange*(float(amatrix[a][b][1])-tvaluereps)/(100-tvaluereps)+20)
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
                            print("found another match",n2.name)
                            #triangle case
                            if(amatrix[neighbors[0]][b]!=0 and amatrix[neighbors[0]][b][0]!="bb"):
                                possiblepoints1=self.getPossiblePoints(circles, neighbors[0],a, amatrix, tvaluereps, tvaluecps)
                                possiblepoints2=self.getPossiblePoints(circles, b,a, amatrix, tvaluereps, tvaluecps)
                                closestpairs=self.optimizePoints(possiblepoints1,possiblepoints2)
                                self.canvas.delete(circles[a])
                                label=n.name
                                newx=(closestpairs[0]+closestpairs[2])/2
                                newy=(closestpairs[1]+closestpairs[3])/2
                                self.createNode(newx, newy, 8, label, circles, a)
                            #line case
                            else:
                                #v case, we will move one of the nodes!
                                if(len(self.getCurrentNeighbors(neighbors[0],a,amatrix))==0 and len(self.getCurrentNeighbors(b,a, amatrix))==0):
                                    self.canvas.delete(circles[b])
                                    circlecenterx=self.canvas.coords(circles[a])[0]+8
                                    circlecentery=self.canvas.coords(circles[a])[1]+8
                                    length = int(lengthrange-lengthrange*(float(amatrix[a][b][1])-tvaluereps)/(100-tvaluereps)+20)
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
                                    listofnodestomove=self.getConnections(b,a,[b],amatrix)
                                    circlecenterx=self.canvas.coords(circles[a])[0]+8
                                    circlecentery=self.canvas.coords(circles[a])[1]+8
                                    length = int(lengthrange-lengthrange*(float(amatrix[a][b][1])-tvaluereps)/(100-tvaluereps)+20)
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
                                    changex=newx-oldcenterx
                                    changey=newy-oldcentery
                                    for c in listofnodestomove:
                                        oldcenterx=self.canvas.coords(circles[c])[0]+8
                                        oldcentery=self.canvas.coords(circles[c])[1]+8
                                        label = nodes[c].name
                                        self.canvas.delete(circles[c])
                                        self.createNode(oldcenterx+changex,oldcentery+changey, 8, label, circles, c) 

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
                    if(amatrix[a][b][1]==0):
                        pass
                    elif(amatrix[a][b][0]=="bb"):
                        pass
                    else:
                        if(amatrix[a][b][0]=="r"):
                            print("is")
                            color='red'
                        elif(amatrix[a][b][0]=="c"):
                            print("is2")
                            color='DeepSkyBlue2'
                        else:
                            print("is3")
                            color='purple'
                        self.connectNodes(a,b,circles[a],circles[b], color, amatrix)

        for circle in circles:
            coords=self.canvas.coords(circle)
            tags1=self.canvas.gettags(circle)
            self.canvas.create_oval(coords[0], coords[1], coords[2], coords[3],fill='green', width=0, tags=tags1)



    
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
    def connectNodes(self,a,b,circle1,circle2, color, amatrix):
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
            self.canvas.itemconfig(l, tags="pi: "+ str(amatrix[a][b][1]) + "\n" + node1 + "        " + node2)


    #right click to get pop up box w info
    def getData(self,event):
        circle = event.widget.find_withtag("current")
        tags_text = ', '.join(self.canvas.gettags(circle))
        top = tk.Toplevel()
        top.title('Datapoint')
        top.geometry("500x100")
        tk.Message(top, text=tags_text, width=500).pack()
        top.after(5000,top.destroy)

    def getPossiblePoints(self,circles, stationary, moving, amatrix, tvaluereps, tvaluecps):
        hypotenuse = int(50-50*(float(amatrix[stationary][moving][1])-tvaluereps)/(100-tvaluereps)+20)
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

    
    def getConnections(self,a,current,listOfConnections,amatrix):
        neighbors=self.getCurrentNeighbors(a,current,amatrix)
        for neighbor in neighbors:
            if(listOfConnections.count(neighbor)==0):
                listOfConnections.append(neighbor)
                listofConnections=self.getConnections(neighbor,current, listOfConnections, amatrix)
        return listOfConnections
    
    def getDrawnNeighbors(self, a, amatrix):
        neighbors=[]
        for b in range(a):
            if(amatrix[a][b][1]!=0 and amatrix[a][b][0]!="bb"):
                neighbors.append(b)
        return neighbors


    def getCurrentNeighbors(self, a, current, amatrix):
        neighbors=[]
        for b in range(current):
            if(amatrix[a][b][1]!=0 and amatrix[a][b][0]!="bb" and b!=a):
                neighbors.append(b)
        return neighbors

    def getMatrix(self,s,t,tvaluereps,tvaluecps):

        array1 = s.split(" ")
        array2 = t.split(" ")

        array1nums = []
        array2nums = []

        onezero = []
        twozero = []

        count = 1
        count2 = 0

        final = []

        real = []

        namesonly = []
        datasetcps = []
        dd = []
        datasetreps = []

        for i in array1:
            if(len(i) == 1):
                pass
            elif(len(i) == 2):
                pass
            elif(len(i) == 3):
                pass
            elif(len(i) == 4):
                cc = i[3]
                if(cc == ":"):
                    pass
                else:
                    array1nums.append(float(i))
            elif(len(i) == 5):
                array1nums.append(float(i))
            elif(len(i) == 6):
                array1nums.append(float(i))
            elif(len(i) == 7):
                array1nums.append(float(i))
            elif(len(i) == 8):
                array1nums.append(float(i))
            elif(len(i) > 10):
                array1nums.append(i)


        for i in array2:
            if(len(i) == 1):
                pass
            elif(len(i) == 2):
                pass
            elif(len(i) == 3):
                pass
            elif(len(i) == 4):
                cc = i[3]
                if(cc == ":"):
                    pass
                else:
                    array2nums.append(float(i))
            elif(len(i) == 5):
                array2nums.append(float(i))
            elif(len(i) == 6):
                array2nums.append(float(i))
            elif(len(i) == 7):
                array2nums.append(float(i))
            elif(len(i) == 8):
                array2nums.append(float(i))
            elif(len(i) > 10):
                array2nums.append(i)

        for i in array1nums:
            if(type(i) == float):
                if(i < tvaluecps):
                    onezero.append(0.00)
                elif(i >= tvaluecps):
                    onezero.append(i)
            else:
                onezero.append(i)

        for i in array2nums:
            if(type(i) == float):
                if(i < tvaluereps):
                    twozero.append(0.00)
                elif(i >= tvaluereps):
                    twozero.append(i)
            else:
                twozero.append(i)

        for i in twozero:
            if(count % 452 == 0):
                final.append(i)
                for i in range(11):
                    final.append(None)
                count = count +1
            else:
                final.append(i)
                count = count+1
        dsi = []
        for i in array2nums:
            if(count % 452 == 0):
                dsi.append(i)
                for i in range(11):
                    dsi.append(None)
                count = count +1
            else:
                dsi.append(i)
                count = count+1

        ds = []
        for i in dsi:
            if(type(i) == str):
                pass
            else:
                ds.append(i)

        for i in range(213906):
            if(i<7500):
                 if(type(onezero[i]) == str and type(final[i]) == str):
                     val1 = onezero[i]
                     val2 = final[i] 
                     if(val1[0:7] == val2[0:7]):
                         real.append(val1[0:7])
                 elif(type(onezero[i]) == float and type(final[i]) == float):
                     val1 = onezero[i]
                     val2 = final[i]
                     if(val1 == 0 and val2 == 0):
                         real.append(["bb",0])
                     elif(val1 == 0 and val2 !=0):
                         real.append(["r",val2])
                     elif(val1 != 0 and val2 == 0):
                         real.append(["c", val1])
                     elif(val1 !=0 and val2 !=0):
                         sum = val1 + val2
                         avg = sum/2
                         real.append(["b",avg])
                 elif(final[i] is None and onezero[i] == 0):
                     real.append(["c", 0])
                 elif(final[i] is None and onezero[i] !=0):
                     val1 = onezero[i]
                     real.append(["c", val1])

            elif(i >= 7500 and i < 208813):
                if(type(onezero[i]) == str and type(final[i]) == str):
                    val1 = onezero[i]
                    val2 = final[i] 
                    if(val1[0:8] == val2[0:8]):
                        real.append(val1[0:8])
                elif(type(onezero[i]) == float and type(final[i]) == float):
                    val1 = onezero[i]
                    val2 = final[i]
                    if(val1 == 0 and val2 == 0):
                        real.append(["bb",0])
                    elif(val1 == 0 and val2 !=0):
                        real.append(["r",val2])
                    elif(val1 != 0 and val2 == 0):
                       real.append(["c", val1])
                    elif(val1 !=0 and val2 !=0):
                        sum = val1 + val2
                        avg = sum/2
                        real.append(["b",avg])
                elif(final[i] is None and onezero[i] == 0):
                    real.append(["c", 0])
                elif(final[i] is None and onezero[i] !=0):
                    val1 = onezero[i]
                    real.append(["c", val1])
            else:
                if(type(onezero[i]) == str):
                    val1 = onezero[i]
                    real.append(val1[0:10])
                elif(onezero[i] == 0):
                    val1 = onezero[i]
                    real.append(["c", val1])
                elif(onezero[i] > 0):
                    val1 = onezero[i]
                    real.append(["c",val1])

        for i in real:
            if(type(i) == str):
                if(i.startswith("C")):
                    namesonly.append(i)

        dataset1 = []

        for i in array1nums:
            if(type(i) == str):
                pass
            else:
                dataset1.append(i)

        factor = 1
        start = 0
        end = 0
        for i in range(463):
            if(i==0):
                continue
            start = end
            end = 462 * i
            n = dataset1[start:end]
            datasetcps.append(n)
            factor = factor + 1

        for i in range(463):
            if(i==0):
                continue
            start = end
            end = 462 * i
            n = ds[start:end]
            dd.append(n)
            factor = factor + 1

        g = ds[0:462]
        dd[0] = g


        for i in dd:
            if(i == []):
                for z in range(462):
                    i.append(None)
                datasetreps.append(i)
            else:
                datasetreps.append(i)

        noname = []


        for i in real:
            if(type(i) != str):
                noname.append(i)

        amatrix = []

        y = 0
        z = 462
        for i in range(462):
            ai = noname[y:z]
            amatrix.append(ai)
            y = y + 462
            z = z + 462

        finalmatrix = []
        finalmatrix.append(amatrix)
        finalmatrix.append(namesonly)
        finalmatrix.append(datasetreps)
        finalmatrix.append(datasetcps)

        return finalmatrix


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
