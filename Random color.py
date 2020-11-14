# Importing of modules.
import random as r
from tkinter import *

seed = 41213872

r.seed(seed) # Sets the starting seed to allow for reproduction of experiment.

# Initialization of variables responsible for the color generation code.
hex_color = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
color_list = []
colors_dict = {
"white": "#ffffff",
"green" : "#00ff00",
"red" : "#ff0000",
"blue" : "#0000ff",
"orange" : "#ffa500",
"purple" : "#800080",
"yellow" : "#ffff00",
"black":"#000000"
}

used_colors = []
init_color_list = []

time_delay = 60000 # Time (in milliseconds) that any color stays on screen.

def create_color_list(colors, init_color_list = init_color_list, samples = hex_color, list_length = 100):
    '''
    This function generates a random list of colors and parses user input adding the respective colors to the list.

    When this function is called, if the 'colors' argument is empty it will create a pseudo-random list of color hex codes that are added to the 
    'color_list' list. Otherwise, it will parse the user's input and compare it to the dictionary of pre-selected colors, if it finds a match it
    will add the respective hex color code to the 'init_color_list' list and will populate the 'color_list' with remaining items until "list_length"
    is reached.

    Parameters:
        - colors: User input.
        - init_color_list: Global variable, stores the colors resulting from the parsing of User Input.
        - samples: Hex code values used to generate the color list.
        - list_length: Total length of the lists, the sum of the lenghts of 'init_color_list' and 'color_list' has to add up to this value. 

    Returns:
        Void.

    '''

    color = ""
    init_colors=0
    a_color_list = []
    colors = colors.replace("Y", "")
    colors = colors.strip() 
    if colors != "":
        a_color_list = colors.split(" ")
        for color in a_color_list:
            if color in colors_dict.keys():
                init_color_list.append(colors_dict.get(color))
        init_colors = len(init_color_list)

    

    i = list_length - init_colors    
    while i >= 0:
        color = ''
        color = "#"+color.join(r.sample(samples,6))
        color_list.append(color)
        i-=1


def set_to_white():
    '''
    Switches current background of the window to white, then continues execution.

    This function sets the background of the current tkinter window to the color white, it will then wait the length of time specified in the variable
    'time_delay'. After it completes this task, it will jump execution to the function 'change_color'.

    Parameters:
        None.
    
    Returns:
        Void.
    '''
    gui['bg'] = colors_dict['white']
    gui.after(time_delay,change_color)

def change_color(color_lists = (color_list,init_color_list,used_colors)):
    '''
    Switches current background of the window to a color from the 'init_color_list' or 'color_list', then continues execution.

    This function sets the background of the current tkinter window to a color. If the list 'init_color_list' is not empty, it will pseudo-randomly select
    one of the colors of the list, change the background to it, and remove it from the list thereafter. Otherwise, it will select the first item of the 
    'color_list' list, change the background to it, and remove it from the list therafter.
    Independent of which list was used the selected color will have its corresponding colorcode added to the 'used_colors' list.

    Parameters:
        color_lists = a set of lists used by this function, that includes 'color_list' (the pre-generated random color list), 'init_color_list' (the color
        list created from user input), and used_colors (the record of all colors used.)
    
    Returns:
        Void.
    '''
    if len(init_color_list) !=0 :
        index = r.randint(0, len(init_color_list)-1)
        color = init_color_list.pop(index)
        used_colors.append(color)
    else:
        color = color_list.pop(0)
        used_colors.append(color)
        
    gui.configure(bg = color)
    gui.after(time_delay, set_to_white)
    
#User Input
key =input("Start? [Y/N]:")
while "Y" not in key: #This loop runs until "Y" is entered or until "N" is entered, in which case it will quit the script.
    if key == "N":
        quit()
    else:
        key =input("Start? [Y/N]:")
    
    continue
else:
    #Initializes color generation routine based on User Input.
    create_color_list(colors=key)    


#Start of the tkinter window routine.
gui = Tk(className="Random Color Bioelectricity Experiment") #Creates the new window object and names it.

#Obtains the screen's dimentions and resizes the window accordingly.
screen_width = str(gui.winfo_screenwidth())
screen_height = str(gui.winfo_screenheight())

gui.geometry(screen_width+"x"+screen_height)
gui.attributes("-topmost", True)

#Start of the color changing routine.
set_to_white()

gui.mainloop()# End of tkinter Windor routine.

with open("color_list.txt",'w+') as f: # Exports the color list to a file.
    for color in used_colors:
        f.write(color+"\n")
        
