# This is a sample Python script.
from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
import zipfile
import shutil

"""
ouverture d un dossier spacéfié en explorateur fichier :
path="C:/Users"
path=os.path.realpath(path)
os.startfile(path)

ouverture d un dossier :
actuelle = os.path.expanduser("~")
    window.filname = filedialog.askopenfilename(initialdir=actuelle, title="Selectionné une fichier ",
                                                filetypes=[('csv files', '*.csv')])

"""



class my_zip_manager():
    def __init__(self):
        self.fenetre = Tk()
        self.bg_color = "#320432"
        self.fg_color = "white"
        # configuration fenetre :
        self.fenetre.geometry("900x460")
        self.fenetre.config(background=self.bg_color)
        self.fenetre.resizable(0, 0)
        self.fenetre.iconbitmap("Images/icons8-zip-50.ico")
        self.fenetre.title(' Zip Manager 1.0 ')
        # --------> Insertion d image au canva :
        my_image = Image.open('Images/icons8-zip-64.png')
        my_icon = ImageTk.PhotoImage(my_image)
        self.canva_image = Label(self.fenetre, image=my_icon, height=120, width=120, bg=self.bg_color)
        self.canva_image.image = my_icon
        self.Label_h1 = Label(self.fenetre, text="Zip Manager", font="Helvetica 20 underline",
                              bg=self.bg_color, fg=self.fg_color)
        self.label_powerd_by = Label(self.fenetre, text="Powerd By Chopen ", font="italic 10 underline", fg=self.fg_color,
                                    bg=self.bg_color, bd=0)
        self.compresser_label = Label(self.fenetre, text="Compression ", font="Courrier 14 italic" , fg=self.fg_color,
                                    bg=self.bg_color, bd=0)
        my_image = Image.open('Images/TextBox_Bg.png')
        my_icon = ImageTk.PhotoImage(my_image)
        self.path = StringVar()
        self.path_extract = StringVar()
        self.canva = Label(self.fenetre, image=my_icon, height=55, width=350, bg=self.bg_color)
        self.canva.image = my_icon
        self.label_path = Label(self.canva, text="Path field", font="Helvetica 12 italic underline",
                                bg=self.fg_color, fg=self.bg_color)
        self.path_entry = Entry(self.canva, textvariable=self.path, font=("Courrier", 13),  fg=self.bg_color,
                                bg=self.fg_color, width=37, bd=0, state='readonly')
        self.select_path_button = Button(self.fenetre, text="Select path", font="Courrier 10 underline",
                                        bg=self.bg_color, fg=self.fg_color, bd=0, command=self.select_path)
        # Partie du code pour extractions :
        self.frame_extract_part = Frame(self.fenetre, bg=self.fg_color, bd=1, width=10, height=370)
        self.extract_label = Label(self.fenetre, text="Extract ", font="Courrier 14 italic" , fg=self.fg_color,
                                    bg=self.bg_color, bd=0)
        self.canva_extract = Label(self.fenetre, image=my_icon, height=55, width=350, bg=self.bg_color)
        self.canva_extract.image = my_icon
        self.label_path_extract = Label(self.canva_extract, text="Path field", font="Helvetica 12 italic underline",
                                bg=self.fg_color, fg=self.bg_color)
        self.path_entry_extarct = Entry(self.canva_extract, textvariable=self.path_extract, font=("Courrier", 13),  fg=self.bg_color,
                                bg=self.fg_color, width=37, bd=0, state='readonly')
        self.select_path_extract_button = Button(self.fenetre, text="Select path", font="Courrier 10 underline",
                                        bg=self.bg_color, fg=self.fg_color, bd=0, command=self.select_extract_files)
        # placer les elements dans la fenetre :
        self.Label_h1.place(relx=0.12, rely=0.1)
        self.canva_image.place(relx=0.01, rely=0.01)
        self.compresser_label.place(relx=0.12, rely=0.26)
        self.canva.place(relx=0.12, rely=0.35)
        self.label_path.place(relx=0.01, rely=0.01)
        self.path_entry.place(relx=0.01, rely=0.4)
        self.select_path_button.place(relx=0.45, rely=0.48)
        self.frame_extract_part.place(relx=0.55, rely=0.1)
        self.extract_label.place(relx=0.58, rely=0.26)
        self.canva_extract.place(relx=0.58, rely=0.35)
        self.label_path_extract.place(relx=0.01, rely=0.01)
        self.path_entry_extarct.place(relx=0.01, rely=0.4)
        self.select_path_extract_button.place(relx=0.91, rely=0.48)
        self.label_powerd_by.place(relx=0.49, rely=0.91)
    def select_path(self):
        actuelle = os.path.expanduser("~")
        self.fenetre.dirname = filedialog.askdirectory(initialdir=actuelle, title="Select folder ")
        if not self.fenetre.dirname == "":
            self.select_path_button['state'] = "disabled"
            self.path.set(self.fenetre.dirname)
            askyesno = messagebox.askyesno("to confirm", "continue with this folder")
            if askyesno == True:
                dirname = str(self.fenetre.dirname).split('/')[-1]
                liste = str(self.fenetre.dirname).split('/')[:-1]
                str_path = ""
                for element in liste:
                    str_path +=str(element)+"/"
                print(liste)
                self.opened_dir = os.listdir(self.fenetre.dirname)
                with zipfile.ZipFile(str(str_path)+str(dirname)+str('.zip'), 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
                    for itr in self.opened_dir:
                        if os.path.isfile(str(self.fenetre.dirname)+"/"+str(itr)):
                            print(str(self.fenetre.dirname))
                            try:
                                my_zip.write(str(self.fenetre.dirname)+"/"+str(itr))
                                print("\n"+str(itr)+"    : Completed")
                            except Exception as e:
                                messagebox.showerror("ERROR!", e)
                messagebox.showinfo("Info !", "Compression Completed")
                askyesno = messagebox.askyesno("Open Folder ", "Open Folder With File Explorers ? ")
                if askyesno==True:
                    path= str(str_path)+str(dirname)+str('.zip')
                    path=os.path.realpath(path)
                    os.startfile(path)
                self.path_entry['state'] = "normal"
                self.path_entry.delete(0, 'end')
                self.select_path_button['state'] = "normal"
                self.path_entry['state'] = "readonly"
            else:
                self.path_entry['state'] = "normal"
                self.path_entry.delete(0, 'end')
                self.select_path_button['state'] = "normal"
                self.path_entry['state'] = "readonly"
        else:
            messagebox.showerror("ERROR!", " Folder selected not found !")
            self.path_entry.delete(0, 'end')
            self.select_path_button['state'] = "normal"
        return
    def select_extract_files(self):
        actuelle = os.path.expanduser("~")
        self.fenetre.filname = filedialog.askopenfilename(initialdir=actuelle, title="Select file ",
                                                filetypes=[('zip files', '*.zip'),('rar files', '*.rar'), ('tar files', '*.tar')])
        if not self.fenetre.filname == "":
            self.select_path_extract_button['state'] = "disabled"
            self.path_extract.set(self.fenetre.filname)
            askyesno = messagebox.askyesno("to confirm", "continue with this files")
            if askyesno == True:
                liste = str(self.fenetre.filname).split('/')[:-1]
                str_path = ""
                for element in liste:
                    str_path +=str(element)+"/"
                with zipfile.ZipFile(self.fenetre.filname, 'r', compression=zipfile.ZIP_DEFLATED) as my_zip:
                    try:
                        my_zip.extractall(str_path+str(self.fenetre.filname).split('/')[-1].split('.')[0])
                        messagebox.showinfo("Info !", "Extraction Completed")
                        opened_dir =os.listdir(str_path+str(self.fenetre.filname).split('/')[-1].split('.')[0])
                        #for element in opened_dir:
                            #if not os.path.isfile(str_path+str(self.fenetre.filname).split('/')[-1].split('.')[0]+"/"+element):
                                #os.rmdir(str_path+str(self.fenetre.filname).split('/')[-1].split('.')[0]+"/"+element)
                        askyesno = messagebox.askyesno("Open Folder ", "Open Folder With File Explorers ? ")
                        if askyesno==True:
                            path= str_path+str(self.fenetre.filname).split('/')[-1].split('.')[0]
                            path=os.path.realpath(path)
                            os.startfile(path)
                    except Exception as e:
                        messagebox.showerror("ERROR!", e)
                    finally:
                        self.path_entry_extarct['state'] = "normal"
                        self.path_entry_extarct.delete(0, 'end')
                        self.select_path_extract_button['state'] = "normal"
                        self.path_entry_extarct['state'] = "readonly"        
            else:
                self.path_entry_extarct['state'] = "normal"
                self.path_entry_extarct.delete(0, 'end')
                self.select_path_extract_button['state'] = "normal"
                self.path_entry_extarct['state'] = "readonly"   
        else:
            messagebox.showerror("ERROR!", " Files selected not found !")
            self.path_entry_extarct.delete(0, 'end')
            self.select_path_extract_button['state'] = "normal"
        return

    def run(self):
        self.fenetre.mainloop()
        return



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = my_zip_manager()
    app.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
