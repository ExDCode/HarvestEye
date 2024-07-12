import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class SidebarCrop(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.color_of_the_gradient = '#8C953C'
        self.configure(bg=self.color_of_the_gradient)

        self.renderSidebarContent()

        ###################################################################


    def renderSidebarContent(self):
        # Destroy everything to re-render
        print("render started")
        for widget in self.winfo_children():
            print("Destroyed")
            widget.destroy()

        # Load the BACK button
        image_path = "./assets/datatype-select/"
        #print(image_path)
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn-back_sm.png"))
        btn_back = tk.Label(self, image=photo )
        btn_back.image = photo
        btn_back.pack(side="top", expand=False, padx=10, pady=10, anchor="nw")
        btn_back.bind('<Button-1>', self.backButton)
        btn_back.configure(bg=self.color_of_the_gradient)



        # Passing a name of the crop as part of the path where assets have same name
        image_path = "./assets/crops/" + self.controller.crop + "/"
        #print(f"self.controller.crop (again) = {self.controller.crop}")
        #print(f"Once again, image_path: {image_path}")

        # Load CHILI TEXT for the side sidebar 
        photo = ImageTk.PhotoImage(Image.open(image_path+"txt_crop_sm.png"))
        txt_chilititle = tk.Label(self, image=photo )
        txt_chilititle.image = photo
        txt_chilititle.pack(side="top", fill="x", expand=True, pady=50)
        txt_chilititle.configure(bg=self.color_of_the_gradient)
        #image_path = "./assets/datatype-select/"

        # Load CHILI image for the side sidebar
        photo = ImageTk.PhotoImage(Image.open(image_path+"img_crop_sm.png"))
        img_chili = tk.Label(self, image=photo )
        img_chili.image = photo
        img_chili.pack(side="top", fill="both", expand=True, pady=50)
        img_chili.configure(bg=self.color_of_the_gradient)

        # Load CHILI TXT INFO for the side sidebar
        photo = ImageTk.PhotoImage(Image.open(image_path+"txt_info_sm.png"))
        txt_chiliinfo = tk.Label(self, image=photo )
        txt_chiliinfo.image = photo
        txt_chiliinfo.pack(side="bottom", fill="y",  expand=True, pady=30, padx=10)
        txt_chiliinfo.configure(bg=self.color_of_the_gradient)




    def backButton(self, event):
        try:
            self.controller.show_frame(self.controller.back_history.pop())
        except:
            print("Nowhere to go. Back button stack is empty")
            self.controller.show_frame("SplashScreen")

        #self.controller.show_frame("DataTypeSelectionScreen")
