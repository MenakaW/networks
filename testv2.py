from collections import namedtuple
import tkinter as tk
from random import seed
from random import randint
import math

correctrep = open(r"correctorderpirep.txt", "r")
correctcp = open(r"correctorderpicp.txt", "r")
referencerep = open(r"unorderpirep.txt","r")
referencecp = open(r"unorderpicp.txt", "r")


input1 = correctrep.read().split()
input2 = correctcp.read().split()
input3 = referencerep.read().split()
input4 = referencecp.read().split()

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
#print(len(namesonlyrep), len(datasetrep), len(numsonlyrep))

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
#print(len(namesonlycp), len(datasetcp), len(numsonlycp))
        
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
thresholdrep = 90
thresholdcp = 80
adjacencymatrix = []
for a in range(414):
    currentmatrix = []
    for b in range(414):
        if(a>404):
            if(b==401 or b==403):
                currentmatrix.append(None)
            else:
                #these have cp vals but not
                n1 = nodes[a]
                n2 = nodes[b]
                cp = n1.cppi[conversionchartcp[b-2][1]]
                if(float(cp)>=thresholdcp):
                    currentmatrix.append(["c",cp])
                else:
                    currentmatrix.append(["n",0])
        elif(b>404):
            if(a==401 or a==403):
                currentmatrix.append(None)
            else:
                n1 = nodes[a]
                n2 = nodes[b]
                cp = n1.cppi[conversionchartcp[b-2][1]]
                if(float(cp)>=thresholdcp):
                    currentmatrix.append(["c",cp])
                else:
                    currentmatrix.append(["n","0"])
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
        else:
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

print(len(adjacencymatrix), len(currentmatrix))

#we define all methods in this block



#initialize our root and tkinter


class Example(tk.Frame):
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

        circles = []

        for circle in nodes:
            label = circle.name
            num = randint(8,1592)
            num2 = randint(8,892)
            rad = 8
            self.createNode(num, num2, rad, label, circles)

             
        for a in range(414):
            for b in range(414):
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
                    self.connectNodes(a,b,circles[a],circles[b], self.canvas, color)

        # This is what enables using the mouse:
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)
        self.canvas.bind("<Button-3>", self.getData)
        #linux scroll
        self.canvas.bind("<Button-4>", self.zoomerP)
        self.canvas.bind("<Button-5>", self.zoomerM)
        #windows scroll
        self.canvas.bind("<MouseWheel>",self.zoomer)

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

    def createNode(self, centerx, centery, radius,label, circles):
        o = self.canvas.create_oval(centerx-radius, centery-radius, centerx+radius, centery+radius, fill = "green", width = 0, tags = label)
        circles.append(o)

    def connectNodes(self,a,b,circle1,circle2,canvas, color):
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
            length = math.sqrt(deltay*deltay+deltax*deltax)
            self.canvas.itemconfig(l, tags="pi: "+ str(adjacencymatrix[a][b][1]) + "\n" + node1 + "        " + node2)
            print(self.canvas.gettags(l))

    def getData(self,event):
        circle = event.widget.find_withtag("current")
        tags_text = ', '.join(self.canvas.gettags(circle))
        top = tk.Toplevel()
        top.title('Datapoint')
        top.geometry("500x100")
        tk.Message(top, text=tags_text, width=500).pack()
        top.after(5000,top.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()







#draw a circle for each node
