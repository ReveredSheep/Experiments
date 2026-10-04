import math
import matplotlib.pyplot as plt

class K3L:
    def __init__(self):
        self.make_objects()
        self.xmax = 10 
        self.ymax = 30

    def make_objects(self):
        self.nlist = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
        self.alist = [0.39,0.72,1,1.52,5.2,9.57,19.2,30.2,39.2] # AU
        self.plist = [0.24,0.61,1,1.88,11.9,29.4,83.7,163.7,247.9] #Yrs
        
        self.jnlist = ['Io','Europa','Ganymede','Callisto']
        self.jalist = [0.42,0.67,1.07,1.88] # million km
        self.jplist = [1.76,3.52,7.15,16.7] # days

    def plot_raw_data(self):
        plt.plot(self.alist[0:6], self.plist[0:6],'o')
        plt.show()

    def plot_polys(self):
        xlist = list(range(0,11))
        p1 = [x for x in xlist]
        p2 = [x**2 for x in xlist]
        plt.plot(xlist, p1, linestyle='dotted', label='1.0')
        plt.plot(xlist, p2, linestyle='dashdot', label='1.2')
        self.set_plt_lims(plt,0,self.xmax,0,self.ymax)

    def plot_raw_plus_poly(self):
        plt.plot(self.alist[0:6], self.plist[0:6],'o')
        self.plot_polys()
        xlist = list(range(0,11))
        p15 = [x**1.5 for x in xlist]
        plt.plot(xlist, p15, linestyle='solid', label="1.5")
        plt.show()
        
    def planet_and_galilean_moons_scaled_plot(self):
        mydpi=120
        fig = plt.figure(figsize=(1200/mydpi,1000/mydpi),dpi=mydpi)
        plt.title("Solar System Planets and Galilean Moons: P vs a")
        plt.xlabel('Distance')
        plt.ylabel('Period')
        pj = [p/1.76 for p in self.jplist]
        aj = [a/0.42 for a in self.jalist]
        plt.scatter(aj[0:7], pj[0:7], facecolors='none', edgecolor='blue', label = 'Galilean Moons')
        xlist = list(range(0,11))
        plt.plot(self.alist[0:6], self.plist[0:6], '+', color = 'black', label='Planets')
        xlist = list(range(0,11))
        p15 = [x**1.5 for x in xlist]
        plt.plot(xlist, p15, linestyle='dashed', color='green', label="1.5")
        plt.legend()
        plt.show()
        plt.savefig('./Fig 2.2.jpg',dpi = mydpi)
        
    def log_log_planet_and_galilean_moons_plot(self):
        mydpi=120
        fig = plt.figure(figsize=(1200/mydpi,1000/mydpi),dpi=mydpi)
        plt.title("Solar System and Galilean Moons: log(P) vs Log(a)")
        plt.xlabel('Log(a)')
        plt.ylabel('Log(P)')
        pj = [math.log10(p) for p in self.jplist]
        aj = [math.log10(a) for a in self.jalist]
        plt.scatter(aj[0:7], pj[0:7],facecolors='none',edgecolor='blue', label = 'Galilean Moons')
        ap = [math.log10(x0) for x0 in self.alist]
        pp = [math.log10(p0) for p0 in self.plist]
        plt.plot(ap,pp,'+',color='black',label='Planets')
        plt.legend()
        plt.show()
        plt.savefig('./Fig 2.3.jpg', dpi=mydpi)
        
    def set_plt_lims(self,plt,xmin,xmax,ymin,ymax):
        ax = plt.gca()
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        
    def make_planet_panel(self):
        mydpi = 100
        fig = plt.figure(figsize=(1200/mydpi,1200/mydpi),dpi=mydpi)
        fig.subplots_adjust(wspace=.1, hspace=.5)
        fig.suptitle("Verifying Kepler's 3rd Law")
        
        plt.subplot(3,1,1)
        plt.xlabel('a (AU)')
        plt.ylabel('P (yrs)')
        plt.title("Solar System Planets (raw data): P vs a")
        self.plot_raw_data
        
        plt.subplot(3,1,2)
        plt.xlabel('a (AU)')
        plt.ylabel('P (yrs)')
        plt.title("Comparison Power Law Curves")
        self.plot_polys()
        plt.legend(title='Powers')
        
        plt.subplot(3,1,3)
        plt.xlabel('a (AU)')
        plt.ylabel('P (yrs)')
        plt.title("Raw data and power-laws 1,.5, and 2.0")
        self.plot_raw_plus_poly()
        plt.legend(title='Powers')
        
        plt.show
        plt.savefig('./Fig 2.1.jpg', dpi = mydpi)
        
if __name__ == '__main__':
    k3l = K3L()
    
    k3l.make_planet_panel()
    k3l.planet_and_galilean_moons_scaled_plot()
    k3l.log_log_planet_and_galilean_moons_plot()