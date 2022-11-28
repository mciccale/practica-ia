import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
LARGE_FONT=("Verdana",12)

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
        for F in(StartPage,Page):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame=self.frames[cont]
        frame.tkraise()
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button=ttk.Button(self,text="Visit Graph Page", command=lambda:controller.show_frame(Page))
        button.pack()
class Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button=ttk.Button(self,text="Back to Home", command=lambda:controller.show_frame(StartPage))
        button.pack()
        f=plt.figure(figsize=(5,5), dpi=100)
        G = nx.petersen_graph() #Aqui iría nuestro grafo calculado
        options = { #Lo podríamos cambiar para que no fuera tan desagradable de ver
        'node_color': 'black',
        'node_size': 100,
        'width': 3,
        }
        f.add_subplot(111)
        nx.draw_random(G, **options)
        canvas=FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH, expand=True)

app=Graphapp()
app.mainloop()