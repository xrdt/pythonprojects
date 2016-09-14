from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from Tkinter import * 

master = Tk()

pop = [.01]
r = 3.1 
t = [0]

for i in range(0, 25):
    pop.append(r * pop[i] * (1 - pop[i]))
    t.append(t[i] + 1)
    i += 1

f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)
a.plot(t, pop)


dataPlot = FigureCanvasTkAgg(f, master=master)
dataPlot.show()
dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

master.mainloop()
