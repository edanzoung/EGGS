#=====================================================#
#=========== EGGS by Edanzoung =====#
#============== edanzoung@outlook.fr =================#
#=====================================================#


#=====================================================#
#==================== LICENSE ========================#

#************** THIS PROJECT IS FREE *****************#
#******* It means that the users have the freedom ****#
#***** *** to run, copy, distribute, study, change ***#
#*********** and improve the software  ***************#
#=====================================================#


from tkinter import Tk, Canvas, Entry, Label, Button, Frame
from PIL import Image, ImageTk, ImageGrab


class Tkinter_app():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x500")
        self.window.configure(bg = "#000")
        self.window.resizable(False, False)
        
        #=== Logo Image
        self.logo_file = Image.open("assets/logo.png")
        self.logo_file = self.logo_file.resize((300,300), Image.ANTIALIAS)
        self.logo=ImageTk.PhotoImage(self.logo_file)
        
        #=== Snake Image/ Sleeping
        self.snake_file = Image.open("assets/snake.png")
        self.snake_file = self.snake_file.resize((300,300), Image.ANTIALIAS)
        self.snake_=ImageTk.PhotoImage(self.snake_file)
        #=== Snake2 Image/ Wake up
        self.snake2_file = Image.open("assets/snake2.png")
        self.snake2_file = self.snake2_file.resize((300,300), Image.ANTIALIAS)
        self.snake2_=ImageTk.PhotoImage(self.snake2_file)
        #=== Snake3 Image/ Angry
        self.snake3_file = Image.open("assets/snake3.png")
        self.snake3_file = self.snake3_file.resize((300,300), Image.ANTIALIAS)
        self.snake3_=ImageTk.PhotoImage(self.snake3_file)
        #=== Snake speech1 Image
        self.speech1_file = Image.open("assets/speech1.png")
        self.speech1_file = self.speech1_file.resize((150,100), Image.ANTIALIAS)
        self.speech1_=ImageTk.PhotoImage(self.speech1_file)
        #=== Snake speech2 Image
        self.speech2_file = Image.open("assets/speech2.png")
        self.speech2_file = self.speech2_file.resize((150,100), Image.ANTIALIAS)
        self.speech2_=ImageTk.PhotoImage(self.speech2_file)
        #=== Snake speech3 Image
        self.speech3_file = Image.open("assets/speech3.png")
        self.speech3_file = self.speech3_file.resize((150,100), Image.ANTIALIAS)
        self.speech3_=ImageTk.PhotoImage(self.speech3_file)
        #=== Snake speech4 Image
        self.speech4_file = Image.open("assets/speech4.png")
        self.speech4_file = self.speech4_file.resize((150,100), Image.ANTIALIAS)
        self.speech4_=ImageTk.PhotoImage(self.speech4_file)
        #=== Snake speech5 Image
        self.speech5_file = Image.open("assets/speech5.png")
        self.speech5_file = self.speech5_file.resize((150,100), Image.ANTIALIAS)
        self.speech5_=ImageTk.PhotoImage(self.speech5_file)
        
        #=== Start Button Image
        self.start_file = Image.open("assets/start.png")
        self.start_file = self.start_file.resize((150,50), Image.ANTIALIAS)
        self.start=ImageTk.PhotoImage(self.start_file)
        #=== Home Button Image
        self.home_file = Image.open("assets/home.png")
        self.home_file = self.home_file.resize((150,50), Image.ANTIALIAS)
        self.home=ImageTk.PhotoImage(self.home_file)

        #=== Egg1 Image
        self.egg_file1 = Image.open("assets/egg1.png")
        self.egg_file1.convert("RGB")
        self.egg_file1 = self.egg_file1.resize((25,30), Image.ANTIALIAS)
        self.egg1_=ImageTk.PhotoImage(self.egg_file1)
        #=== Egg2 Image
        self.egg_file2 = Image.open("assets/egg2.png")
        self.egg_file2.convert("RGB")
        self.egg_file2 = self.egg_file2.resize((25,30), Image.ANTIALIAS)
        self.egg2_=ImageTk.PhotoImage(self.egg_file2)
        #=== Egg3 Image
        self.egg_file3 = Image.open("assets/egg3.png")
        self.egg_file3.convert("RGB")
        self.egg_file3 = self.egg_file3.resize((25,30), Image.ANTIALIAS)
        self.egg3_=ImageTk.PhotoImage(self.egg_file3)
        #=== Egg4 Image
        self.egg_file4 = Image.open("assets/egg4.png")
        self.egg_file4.convert("RGB")
        self.egg_file4 = self.egg_file4.resize((25,30), Image.ANTIALIAS)
        self.egg4_=ImageTk.PhotoImage(self.egg_file4)
        #=== Egg5 Image
        self.egg_file5 = Image.open("assets/egg5.png")
        self.egg_file5.convert("RGB")
        self.egg_file5 = self.egg_file5.resize((25,30), Image.ANTIALIAS)
        self.egg5_=ImageTk.PhotoImage(self.egg_file5)

        #==== Box Color initial background color
        self.color=(0,0,0)
        
        #==== Egg1 coordinates
        self.egg1_coord_x=365
        self.egg1_coord_y=222
        #==== Egg2 coordinates
        self.egg2_coord_x=375
        self.egg2_coord_y=222
        #==== Egg3 coordinates
        self.egg3_coord_x=390
        self.egg3_coord_y=222
        #==== Egg4 coordinates
        self.egg4_coord_x=410
        self.egg4_coord_y=222
        #==== Egg5 coordinates
        self.egg5_coord_x=425
        self.egg5_coord_y=222
        

        self.App()

    def App(self):
        
        
        def rgb(rgb):
            """translate an rgb tuple of int to a tkinter friendly color code"""
            return "#%02x%02x%02x" % rgb

        

        #=====================================================#
        #================= HOME PAGE    ======================#
        #=====================================================#
        self.frame1=Frame(self.window,bg = rgb((255,0,0)), height = 500, width = 800)
        self.frame1.place(x=0,y=0)
        self.canvas = Canvas(self.frame1,bg = "#fff",
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")

        self.canvas.place(x = 0, y = 0)

        #==== Logo Image
        self.canvas.create_image(400,200, image=self.logo)

        #=====================================================#
        #================= HOME PAGE  END  ===================#
        #=====================================================#
        

        #=====================================================#
        #================= SNAKE PAGE    =====================#
        #=====================================================#
        self.frame2=Frame(self.window,bg = rgb((100,100,100)), height = 500, width = 800)
        self.frame2.place(x=0,y=0)
        self.canvas2 = Canvas(self.frame2,bg = rgb((255,255,255)),
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0)
        self.canvas2.place(x = 0, y = 0)

        

        #==== Snake Image
        self.snake=self.canvas2.create_image(400,200, image=self.snake2_)
        #==== Rectangle
        self.screen=self.canvas2.create_rectangle(0,380,100,480,fill=rgb((self.color)))
        self.screen_description=self.canvas2.create_text(90,490,text="",fill=rgb((0,0,0)),font=("Time",11,"bold"))
        #==== Snake speech
        self.snake_speech=self.canvas2.create_image(530,50, image="")
        #==== Egg1 Image
        self.egg1=self.canvas2.create_image(self.egg1_coord_x,self.egg1_coord_y, image=self.egg1_)
        #==== Egg2 Image
        self.egg2=self.canvas2.create_image(self.egg2_coord_x,self.egg2_coord_y, image=self.egg2_)
        #==== Egg3 Image
        self.egg3=self.canvas2.create_image(self.egg3_coord_x,self.egg3_coord_y, image=self.egg3_)
        #==== Egg4 Image
        self.egg4=self.canvas2.create_image(self.egg4_coord_x,self.egg4_coord_y, image=self.egg4_)
        #==== Egg5 Image
        self.egg5=self.canvas2.create_image(self.egg5_coord_x,self.egg5_coord_y, image=self.egg5_)
        
        self.log=self.canvas2.create_text(120,10,text="",fill=rgb((255,255,255)),font=("Time",10,"bold"))
        
        #=====================================================#
        #================= SNAKE PAGE   END ==================#
        #=====================================================#
        

        #=====================================================#
        #================= PAGINATION FUNCTIONS ==============#
        #=====================================================#

        self.frame1.lift()
        
        def begin():
            self.frame2.lift()
            self.frame1.lower()
        def home():
            self.frame1.lift()
            self.frame2.lower()
            

        #==== Button Start in Home Page        
        self.con_button = Button(self.canvas,image=self.start,compound = 'center',relief="flat",
                            highlightthickness = 0,text="",
                            bg=rgb((255,255,255)),borderwidth = 0,cursor="hand2",command=begin)
        self.con_button.place(x=320, y=400)
        
        #==== Button Home in snake Page
        self.decon_button = Button(self.canvas2,image=self.home,compound = 'center',relief="flat",
                            highlightthickness = 0,text="",
                            bg=rgb((255,255,255)),borderwidth = 0,cursor="hand2",command=home)
        self.decon_button.place(x=350, y=420)

        #=====================================================#
        #================= PAGINATION FUNCTIONS  END =========#
        #=====================================================#

        #=====================================================#
        #================= MOUSE EVENTS FUNCTIONS  ===========#
        #=====================================================#

        #==== When Mouse Enter and move over the snake
        def info(event):
            #===== Screen Position Calculation
            x=self.window.winfo_rootx()+self.canvas2.winfo_x()
            y=self.window.winfo_rooty()+self.canvas2.winfo_y()
            x1=x+self.canvas2.winfo_width()
            y1=y+self.canvas2.winfo_height()
            #===== Screen Loading
            screen = ImageGrab.grab(bbox=(x,y,x1,y1)).load()
            
            #===== Screen Pixel color data under the mouse point
            data=screen[event.x,event.y]
            #=== data[0] is red data/data[1] is green data/data[2] is blue data
            color = (data[0],data[1],data[2])         

            #=== color box overview
            self.canvas2.itemconfig(self.screen,fill=rgb(color))
            self.canvas2.itemconfig(self.screen_description,fill=rgb((0,0,0)),text='RGB Color'+': '+str(color))
            
            self.canvas2.itemconfig(self.log,fill=rgb((0,0,0)),text='Mouse coordinates ==> x: '+str(event.x)+' / '+'y: '+str(event.y))
                
        def Snake_color_detection(event):
            
            #self.canvas2.itemconfig(self.snake,image=self.snake_)

            #===== Screen Position Calculation
            x=self.window.winfo_rootx()+self.canvas2.winfo_x()
            y=self.window.winfo_rooty()+self.canvas2.winfo_y()
            x1=x+self.canvas2.winfo_width()
            y1=y+self.canvas2.winfo_height()
            #===== Screen Loading
            screen = ImageGrab.grab(bbox=(x,y,x1,y1)).load()
            
            #===== Screen Pixel color data under the mouse point
            data=screen[event.x,event.y]
            #=== data[0] is red data/data[1] is green data/data[2] is blue data
            color = (data[0],data[1],data[2])
                   
            #=== In our case the snake color code in RGB is (255,127,42)
            if (color==(255,127,42) or color==(0,0,0)):
                self.canvas2.itemconfig(self.snake,image=self.snake2_)
                self.canvas2.itemconfig(self.snake_speech,image="")
            else:
                self.canvas2.itemconfig(self.snake,image=self.snake_)
                self.canvas2.itemconfig(self.snake_speech,image="")

        #==== How to move Eggs
        def egg1_move(event):
            self.egg1_coord_x=event.x
            self.egg1_coord_y=event.y
            
            self.canvas2.coords(self.egg1,(self.egg1_coord_x,self.egg1_coord_y))
            
            if (self.egg1_coord_x<245 or self.egg1_coord_x>560 or self.egg1_coord_y<50 or self.egg1_coord_y>360):
                self.canvas2.itemconfig(self.snake,image=self.snake3_)
                self.canvas2.itemconfig(self.snake_speech,image=self.speech1_)
            else:
                self.canvas2.itemconfig(self.snake,image=self.snake2_)
                self.canvas2.itemconfig(self.snake_speech,image="")

        def egg2_move(event):
            self.egg2_coord_x=event.x
            self.egg2_coord_y=event.y
            
            self.canvas2.coords(self.egg2,(self.egg2_coord_x,self.egg2_coord_y))
            
            if (self.egg2_coord_x<245 or self.egg2_coord_x>560 or self.egg2_coord_y<50 or self.egg2_coord_y>360):
                self.canvas2.itemconfig(self.snake,image=self.snake3_)
                self.canvas2.itemconfig(self.snake_speech,image=self.speech2_)
            else:
                self.canvas2.itemconfig(self.snake,image=self.snake2_)
                self.canvas2.itemconfig(self.snake_speech,image="")

        def egg3_move(event):
            self.egg3_coord_x=event.x
            self.egg3_coord_y=event.y
            
            self.canvas2.coords(self.egg3,(self.egg3_coord_x,self.egg3_coord_y))
            
            if (self.egg3_coord_x<245 or self.egg3_coord_x>560 or self.egg3_coord_y<50 or self.egg3_coord_y>360):
                self.canvas2.itemconfig(self.snake,image=self.snake3_)
                self.canvas2.itemconfig(self.snake_speech,image=self.speech3_)
            else:
                self.canvas2.itemconfig(self.snake,image=self.snake2_)
                self.canvas2.itemconfig(self.snake_speech,image="")

        def egg4_move(event):
            self.egg4_coord_x=event.x
            self.egg4_coord_y=event.y
            
            self.canvas2.coords(self.egg4,(self.egg4_coord_x,self.egg4_coord_y))
            
            if (self.egg4_coord_x<245 or self.egg4_coord_x>560 or self.egg4_coord_y<50 or self.egg4_coord_y>360):
                self.canvas2.itemconfig(self.snake,image=self.snake3_)
                self.canvas2.itemconfig(self.snake_speech,image=self.speech4_)
            else:
                self.canvas2.itemconfig(self.snake,image=self.snake2_)
                self.canvas2.itemconfig(self.snake_speech,image="")

        def egg5_move(event):
            self.egg5_coord_x=event.x
            self.egg5_coord_y=event.y
            
            self.canvas2.coords(self.egg5,(self.egg5_coord_x,self.egg5_coord_y))
            
            if (self.egg5_coord_x<245 or self.egg5_coord_x>560 or self.egg5_coord_y<50 or self.egg5_coord_y>360):
                self.canvas2.itemconfig(self.snake,image=self.snake3_)
                self.canvas2.itemconfig(self.snake_speech,image=self.speech5_)
            else:
                self.canvas2.itemconfig(self.snake,image=self.snake2_)
                self.canvas2.itemconfig(self.snake_speech,image="")

        #=====================================================#
        #================= MOUSE EVENTS FUNCTIONS  END =======#
        #=====================================================#


        #=====================================================#
        #============= ITEMS BINDING =========================#
        #=====================================================#
        self.canvas2.tag_bind(self.egg1,"<B1-Motion>",egg1_move)
        self.canvas2.tag_bind(self.egg2,"<B1-Motion>",egg2_move)
        self.canvas2.tag_bind(self.egg3,"<B1-Motion>",egg3_move)
        self.canvas2.tag_bind(self.egg4,"<B1-Motion>",egg4_move)
        self.canvas2.tag_bind(self.egg5,"<B1-Motion>",egg5_move)
        self.canvas2.tag_bind(self.snake,"<Motion>",Snake_color_detection)
        self.canvas2.bind("<Motion>",info)
        #=====================================================#
        #============= ITEMS BINDING  END ====================#
        #=====================================================#


if __name__=='__main__':
    app=Tkinter_app()
    app.window.mainloop()
