'''
Modue name
----------
graph

Module summary
--------------
Module that simplifies the coding process to plot graphs

Usage
-----
This module is is used to plot different graphs like scatter plot, gaussian plot 
and reduces number of lines of repetitive code. 

Example
-------
Here is an example of how to use this module in projects.
```python
import graph as gr

position_graph =gr.PlotGraph(plot_number=221, y1_data=position[:,0], 
y2_data=position[:,1],title='Position data from sensor', xlabel='Time (s)', 
ylabel='Position (m)',label_1='X-position',label_2='Y-position')

position_graph.scatter_plot()

## Display graph
plt.tight_layout()
plt.show()

```python

Author
------
Gavin Furtado

Role
----
AOCS Engineer
'''
import numpy as np
import matplotlib.pyplot as plt

class PlotGraph(object):
    def __init__(self, plot_number=None, y1_data=None, y2_data=None, y3_data=None,
                 title='Title', xlabel='X-Label', ylabel='Y-Label', 
                 label_1=None,label_2= None,label_3 = None,
                 bins=30, alpha=0.7, density=True):
        self.plot_number = plot_number
        self.y1_data = y1_data
        self.y2_data = y2_data
        self.y3_data = y3_data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.label_1 = label_1
        self.label_2 = label_2
        self.label_3 = label_3
        self.bins = bins
        self.alpha = alpha
        self.density = density
    
    def scatter_plot(self):
        plt.subplot(self.plot_number)
        x_data=np.arange(len(self.y1_data))        
        plt.scatter(x_data, self.y1_data, label = self.label_1)
        plt.scatter(x_data, self.y2_data, label = self.label_2)
        #plt.plot(x_data, self.y3_data, label = self.label_3)
        plt.grid(which='major',color='#DDDDDD',linewidth=0.5)
        plt.grid(which='minor',color='#EEEEEE', linestyle=':',linewidth =0.6)
        plt.minorticks_on()
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()

    def line_plot(self):
        #plt.subplot(self.plot_number)
        x_data=np.arange(len(self.y1_data))        
        plt.plot(x_data, self.y3_data,'g-', label = self.label_3)
        # plt.grid(which='major',color='#DDDDDD',linewidth=0.5)
        # plt.grid(which='minor',color='#EEEEEE', linestyle=':',linewidth =0.6)
        # plt.minorticks_on()
        # plt.xlabel(self.xlabel)
        # plt.ylabel(self.ylabel)
        # plt.title(self.title)
        plt.legend()
    
    def gaussian_plot(self):
        plt.subplot(self.plot_number)
        plt.hist(self.y1_data.flatten(), self.bins, density=self.density, alpha=self.alpha)
        plt.grid(which='major',color='#DDDDDD',linewidth=0.5)
        plt.grid(which='minor',color='#EEEEEE', linestyle=':',linewidth =0.6)
        plt.minorticks_on()
        plt.title(self.title)
        plt.xlabel(self.xlabel) 
        plt.ylabel(self.ylabel)
