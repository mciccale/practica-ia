import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from algorithm import G,algorithm, closed_list
LARGE_FONT=("Verdana",12)
OptionList = [
            'piraeus','faliro','moschato','kallithea','tavros','petralona','thissio','monastiraki', 
            'omonia', 'victoria', 'aghios nikolaos', 'kato patissia', 
            'aghios eleftherios', 'ano patissia', 'perissos', 'pefkakia', 'nea ionia', 'iraklio', 
            'irini', 'neratziotissa', 'maroussi', 'kat', 'kifissia',
            'aghios antonios', 'sepolia', 'attiki', 'larissa st.', 'metaxourghio', 'panepistimio', 
            'syntagma', 'akropoli', 'sygroy - fix', 'neos kosmos', 'aghios ioannis', 
            'dafni', 'aghios dimitrios',
            'egaleo', 'eleonas', 'kerameikos', 'evangelismos', 'megaro moussikis', 'ambelokipi', 'panormou', 
            'katehaki', 'ethniki amyna', 'holargos', 'nomismatokopio', 'aghia paraskevi',
            'halandri', 'douk. plakentias', 'pallini', 'peania - kantza', 'koropi', 'airport',
            
        ] 
class Graphapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.iconbitmap(self, default="")
        tk.Tk.wm_title(self, "Metro Atenas")
        container=tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        frame=StartPage(container,self)
        self.frames[StartPage]=frame
        frame.grid(row=0, column=0, sticky="nsew", padx=100, pady=100, ipadx=100, ipady=100)
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame=self.frames[cont]
        frame.tkraise()
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Start Page", font=LARGE_FONT)
        label.pack(pady=20,padx=90)
        variable = tk.StringVar(self)
        variable.set(OptionList[0])
        opt = tk.OptionMenu(self, variable, *OptionList)
        opt.config(width=15, font=('Helvetica', 12))
        opt.pack()
        opt.place(x=50,y=150)
        variable2 = tk.StringVar(self)
        variable2.set(OptionList[0])
        variable.get
        opt2 = tk.OptionMenu(self, variable2, *OptionList)
        opt2.config(width=15, font=('Helvetica', 12))
        opt2.pack()
        opt2.place(x=250,y=150)
        button=ttk.Button(self,text="Search Path", command=lambda:[algorithm(variable.get(),variable2.get()), Page()])
        button.pack()
class Page(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.iconbitmap(self, default="")
        tk.Tk.wm_title(self, "BEST PATH")
        container=tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        label=tk.Label(self,text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        f=plt.figure(figsize=(15,8), dpi=100)
        layout = {
            'piraeus':[0,2],'faliro':[5,3],'moschato':[7,5],'kallithea':[8,6],'tavros':[10,7],'petralona':[12, 9],'thissio':[12.25, 11],'monastiraki':[12.25, 13], 
            'omonia':[12.25, 15], 'victoria':[12.25,17], 'aghios nikolaos':[10,21], 'kato patissia':[11,22], 
            'aghios eleftherios':[12,24], 'ano patissia':[14.5,25], 'perissos':[16,26], 'pefkakia':[17.5,27], 'nea ionia':[19,28], 'iraklio':[20,29], 
            'irini':[20.5,34], 'neratziotissa':[21,36], 'maroussi':[23,38], 'kat': [25,40], 'kifissia': [27,42],
            'aghios antonios': [5, 24], 'sepolia': [7, 22], 'attiki': [9, 20], 'larissa st.': [9, 18], 'metaxourghio': [9, 16], 'panepistimio': [13.5, 13], 
            'syntagma': [14.5, 12], 'akropoli': [14.5, 10], 'sygroy - fix': [14.5, 8], 'neos kosmos': [14.5, 6], 'aghios ioannis': [14.5, 4], 
            'dafni': [14.5, 2], 'aghios dimitrios': [14.5, 0],
            'egaleo': [2,18], 'eleonas': [5,15], 'kerameikos': [7,13], 'evangelismos':[19, 12], 'megaro moussikis': [20.5,13], 'ambelokipi': [22,14], 'panormou': [23,15], 
            'katehaki': [24,16], 'ethniki amyna': [25,17], 'holargos': [26,18], 'nomismatokopio': [27,19], 'aghia paraskevi': [28,20],
            'halandri': [29,21], 'douk. plakentias': [31,23], 'pallini': [34,21.5], 'peania - kantza': [34,19], 'koropi': [34,13], 'airport':[38,11]
            
        }
        f.add_subplot(111)
        
        color_map = ['green' for node in OptionList ]
        indice: int = 0
        node: str 
        for element in closed_list:
            node=element[2]
            try:
                indice=OptionList.index(node)
                color_map.pop(indice)
                color_map.insert(indice,'red')
            except ValueError:
                print('No esta el nodo ' + node)
        print(color_map)
        nx.draw_networkx(G,layout, node_color=color_map, node_size=50,edge_color='gray', font_size=8)
        canvas=FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH, expand=True)
        color_map.clear()
        closed_list.clear()
app=Graphapp()
app.mainloop()