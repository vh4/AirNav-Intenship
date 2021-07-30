import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("GUI")
        #setting window size
        width=685
        height=577
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_156=tk.Button(root)
        GButton_156["activebackground"] = "#1e90ff"
        GButton_156["activeforeground"] = "black"
        GButton_156["bg"] = "#efefef"
        GButton_156["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=20)
        GButton_156["font"] = ft
        GButton_156["fg"] = "#000000"
        GButton_156["justify"] = "center"
        GButton_156["text"] = "SUBMIT"
        GButton_156.place(x=290,y=360,width=141,height=39)
        GButton_156["command"] = self.GButton_156_command

        GLineEdit_818=tk.Entry(root)
        GLineEdit_818["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=20)
        GLineEdit_818["font"] = ft
        GLineEdit_818["fg"] = "#333333"
        GLineEdit_818["justify"] = "center"
        GLineEdit_818["text"] = "Tulis di sini"
        GLineEdit_818.place(x=130,y=250,width=462,height=59)

        GLabel_106=tk.Label(root)
        GLabel_106["activebackground"] = "#6def35"
        GLabel_106["activeforeground"] = "#51c418"
        ft = tkFont.Font(family='Times',size=38)
        GLabel_106["font"] = ft
        GLabel_106["fg"] = "#c2199b"
        GLabel_106["justify"] = "center"
        GLabel_106["text"] = "TEXT TO SPEECH"
        GLabel_106.place(x=90,y=40,width=505,height=108)
        print(GLineEdit_818.get())
    def GButton_156_command(self):
        print("command su")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
