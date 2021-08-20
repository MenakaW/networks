# networks

Prior to running, you might have to run this command:

sudo apt-get install python3-tk

-------------------Unveiling CP/Reps Data-------------------

in terminal, run ./working.py 

the program will give you 2 prompts. first, it will ask you whether you want edges (lines between the nodes) or not. it will also ask you how many nodes out of 462 you would like to see. if you're unsure try 

chmod +x working.py 

then:

(echo y; echo 462)|./working.py

once you see the window pop up, use the sliders to adjust the rep and cp pi values (ie. rep: 60,cp: 70). there is also an option for length range - a lower range will create tighter clusters, while the higher range will create clusters that are more spread out. once the sliders are to your liking, hit the go button! if nothing seems to be happening, check the terminal, you will which node is being added.

once you have the generated window, right click on nodes(circles) or edges(lines) to get additional data, click and drag to move the network around and scroll to zoom in or out! 


------------------New CP/Reps Data------------

in terminal, run ./updatedtest.py (if you do not have python3, you might want to install that now!)

the program will give you 2 prompts. first, it will ask you whether you want edges (lines between the nodes) or not. it will also ask you how many nodes out of 414 you would like to see. if you're unsure try 

chmod +x updatedtest.py 

then:

(echo y; echo 414)|./updatedtest.py

once you see the window pop up, use the sliders to adjust the rep and cp pi values (ie. rep: 60,cp: 70). there is also an option for length range - a lower range will create tighter clusters, while the higher range will create clusters that are more spread out. once the sliders are to your liking, hit the go button! if nothing seems to be happening, check the terminal, you will which node is being added.

once you have the generated window, right click on nodes(circles) or edges(lines) to get additional data, click and drag to move the network around and scroll to zoom in or out! 
