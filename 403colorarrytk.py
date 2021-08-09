from graphics import *
from tkinter import *
import math
import random


file1 = open(r"pimatrixnewrep.txt","r")
s=file1.read()

array = s.split(" ")

dataset = []

namesonly=[]
numsonly=[]
count = 0
for i in array:

    if(i==""):
        b=1
    elif(i[0].isalpha()):
        count = count+1
        namesonly.append(i)
        if(count>1):
            dataset.append(numsonly)
            numsonly=[]
    elif(i[0]==" "):
        b=1
    elif(i[len(i)-1]==":"):
        b=1
    elif(i[0]=="-"):
        numsonly.append("0")
    else:
        numsonly.append(i)
dataset.append(numsonly)
print(namesonly)
print(len(namesonly))

class Example(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self, width=600, height=600, background="bisque")
        self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,1000,1000))

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        def _from_rgb(rgb):
            return "#%02x%02x%02x" % rgb

        for y in range(403):
            for x in range(y+1):
                rect = Rectangle(Point(2*x,2*y), Point(2*x+2,2*y+2))
                currentdata = float(dataset[x][y])
                numdata =int(math.trunc(currentdata))
                red = 0
                green = 0
                blue = 0
                relative = 0
                if(numdata >48):
                    red = 255
                elif(numdata > 40):
                    relative = (1/(49-numdata))*100
                    red = 255
                    green =255-int(255*relative / 100)
                elif(numdata > 32):
                    relative = (1/(41-numdata))*100
                    green = 255
                    red = int(255*relative/ 100)
                elif(numdata > 24):
                    relative = (1/(33-numdata))*100
                    green = 255
                    blue =255-int(255*relative/ 100)
                elif(numdata > 16):
                    relative = (1/(25-numdata))*100
                    blue = 255
                    green = int(255*relative/100)
                elif(numdata > 8):
                    relative = (1/(17-numdata))*100
                    blue = 255
                    red =255-int(255*relative/100)
                else:
                    relative = (1/(9-numdata))*100
                    red = 255
                    blue = int(255*relative/100)
                rgb = (red,green,blue)
                self.canvas.create_rectangle(2*x,2*y, 2*x+2, 2*y+2, fill=_from_rgb(rgb), width=0, tags="virus1" + namesonly[int(x)] + "\n\nvirus2" + namesonly[int(y)] + "\n\n" + "pairwise identity: " + dataset[int(x)][int(y)] + "%")
                


        

        # This is what enables using the mouse:
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)
        self.canvas.bind("<Button-3>", self.getData)
        #linux scroll
        self.canvas.bind("<Button-4>", self.zoomerP)
        self.canvas.bind("<Button-5>", self.zoomerM)
        #windows scroll
        self.canvas.bind("<MouseWheel>",self.zoomer)

    def getData(self,event):
        rect=event.widget.find_withtag("current")
        tags_text=', '.join(self.canvas.gettags(rect))
        print(tags_text)
        top = tk.Toplevel()
        top.title('Datapoint')
        top.geometry("500x100")
        Message(top, text=tags_text, width=500).pack()
        top.after(5000,top.destroy)
    
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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("New 403 Rep Pi")
    Example(root).pack(fill="both", expand=True)
    root.mainloop()

