from tkinter import *

root = Tk()
root.title ("cross-zero")
canva = Canvas(root, width=700, height=700, bg='#808000')
canva.focus_set ()
canva.pack()

#pole
canva.create_polygon (50,50, 50,650, 650,650, 650,50, fill = '#FFFFE0', width = 2, outline = 'black')
canva.create_polygon (250,50, 450,50, 450,650, 250,650, fill = '#FFFFE0', width = 2, outline = 'black')
canva.create_polygon (50,250, 50,450, 650,450, 650,250, fill = '#FFFFE0', width = 2, outline = 'black')
canva.create_line (250,50, 250,650,  width = 2, fill = "Black")
canva.create_line (450,50, 450,650,  width = 2, fill = "Black")
#mouse coordinates
def getorigin(eventorigin):
    x = eventorigin.x
    y = eventorigin.y
    
    canva.create_oval ((x-100, y-100),(x+100,y+100), width=5, outline = '#FF0000' )


root.bind("<Button 1>",getorigin)
root.mainloop ()