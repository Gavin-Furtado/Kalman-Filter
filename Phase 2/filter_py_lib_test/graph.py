import numpy as np
import matplotlib.pyplot as plt

class PlotGraph(object):
    def __init__(self, plot_number=None, y1_data=None, y2_data=None, 
                 title='Title', xlabel='X-Label', ylabel='Y-Label', 
                 label_1=None,label_2= None,
                 bins=30, alpha=0.7, density=True):
        self.plot_number = plot_number
        self.y1_data = y1_data
        self.y2_data = y2_data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.label_1 = label_1
        self.label_2 = label_2
        self.bins = bins
        self.alpha = alpha
        self.density = density
    
    def scatter_plot(self):
        plt.subplot(self.plot_number)
        x_data=np.arange(len(self.y1_data))        
        plt.scatter(x_data, self.y1_data, label = self.label_1)
        plt.scatter(x_data, self.y2_data, label = self.label_2)
        plt.grid(which='major',color='#DDDDDD',linewidth=0.5)
        plt.grid(which='minor',color='#EEEEEE', linestyle=':',linewidth =0.6)
        plt.minorticks_on()
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
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