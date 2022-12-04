import tkinter as tk
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import networkx as nx
import algorithm as a
from algorithm import reconst_path, G, layout, label_layout

matplotlib.use("TkAgg")
LARGE_FONT=("Verdana",12)

graph1 = a.Graph(a.graph)

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
        a.Graph.__init__(graph1, a.graph)
        button=ttk.Button(self,text="Search Path", command=lambda:[a.Graph.a_star(graph1, variable.get(),variable2.get()), Page()])
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
        f=plt.figure(figsize=(12,6), dpi=200)
        f.add_subplot(111)

        color_map = ['green' for node in OptionList]
        indice: int = 0
        node: str

        for element in reconst_path:
            try:
                indice=OptionList.index(element)
                color_map.pop(indice)
                color_map.insert(indice,'red')
            except ValueError:
                print('No esta el nodo ' + element)

        nx.draw_networkx(G,layout, node_color=color_map, node_size=15,edge_color='gray', with_labels=False)
        nx.draw_networkx_labels(G,pos=label_layout, verticalalignment='center', horizontalalignment='right', font_size=4)
        canvas=FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
        color_map.clear()
        reconst_path.clear()
app=Graphapp()
app.mainloop()
