import numpy as np
import plotext as pltxt
import matplotlib.pyplot as matplt
import os

def parser():
    pass

def CLI_VIEW(expression):
    x = np.linspace(0, 5, 1000)
    y = expression
    pltxt.plot(x, y)
    pltxt.show()

# def GUI_VIEW(expression):
def GUI_VIEW():
    x = np.linspace(0, 5, 10000)
    y = x**2 + 3*x + 2
    matplt.plot(x, y)
    matplt.grid()
    #matplt.show()
    images = os.listdir("Images")
    print(images)
    count = len(images)
    image_name = input("Enter File Name to be Saved (default : image.png) ")
    if len(image_name) == 0:
        matplt.savefig(f"Images/image{count+1}.png", dpi = 300)
    else:
        try:
            matplt.savefig(f"Images/{image_name}.png", dpi = 300)
        except:
            print("Conflict in file name / already used !")



GUI_VIEW()
