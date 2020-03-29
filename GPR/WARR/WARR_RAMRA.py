# Automatically generated by GPRPy
import gprpy.gprpy as gp
mygpr = gp.gprpyCW()
# Loading the data
mygpr.importdata('XLINE35.HD',dtype='WARR')
# Setting the profile. I am guessing that it is 0.6 m to 25 m.
mygpr.adjProfile(0.5,27)
# Only use data down to 300 ns
mygpr.truncateY(300)
# Dewow
mygpr.dewow(99999999999999999999)
# Gain (normalize)
mygpr.normalize()
# Calculating the stacked amplitudes for linear patterns and hyperbolic
# patterns. Velocities are 0.01:0.001:0.35 m/ns
mygpr.linStackedAmplitude(vmin=0.01,vmax=0.35,vint=0.001)
mygpr.hypStackedAmplitude(vmin=0.01,vmax=0.35,vint=0.001)

# Adding the linear pattern we see in the data
mygpr.addLin(zerotwtt=18,vel=0.3) # You can change the travel time and velocity here
mygpr.addLin(zerotwtt=32,vel=0.15) 

# Adding the hyperbolic pattern we see in the data
mygpr.addHyp(zerotwtt=151,vel=0.11)
mygpr.addHyp(zerotwtt=158,vel=0.1)

# Now comes the plotting
# Prepare the data figure
import matplotlib as mpl
import matplotlib.pyplot as plt
# Making font size larger 
plt.rc('font', size=13)


# Images ratio: The larger, the narrower
imgratio = 1.7


### Plotting the data including the hyperbolae / lines
mygpr.showCWFig(color='gray', contrast=6, yrng=[300,10.94], xrng=[0.6,25], showlnhp=True)
# To change some of the properties of the plotted data,
# extract the axes
ax = plt.gca()
# Change the aspect ratio
ax.set_aspect(imgratio/ax.get_data_ratio())
# Put x-axis labels and numbers at bottom
ax.get_xaxis().set_label_position('bottom')
ax.get_xaxis().set_ticks_position('bottom')
# Put y-axis label and numbers at right
ax.get_yaxis().set_label_position('right')
ax.get_yaxis().set_ticks_position('right')
# Set title
ax.set_title('data')

# Change color of line 1
# You can change width, everything the way you want
# The first one id the airwave, because you added it the first
ax.lines[0].set(color=[0,0.7,1],linestyle='--',linewidth=2)
# Then the ground wave
ax.lines[2].set(color=[1,0.5,0],linestyle='--',linewidth=2)
# Next comes the first hyperbola
ax.lines[4].set(color=[0,1,0],linestyle='--',linewidth=2)
# Finally, the second hyperbola
ax.lines[6].set(color=[0,1,0],linestyle='--',linewidth=2)
# Other possibilities for color:
# [0.8,1,0.4]
# [0.8,0.8,0.4]
# [0,1,0]

# Clear the smaller lines drawn on top of the bigger ones for visibility
ax.lines[7].remove()
ax.lines[5].remove()
ax.lines[3].remove()
ax.lines[1].remove()

# Make a pdf
plt.savefig('WARRdata.pdf',dpi=600)



### These are the stacked amplitude figures
# First the linear
mygpr.showStAmpFig(whichstamp='lin', saturation=2, yrng=[300,10.94], vrng=[0.01,0.35])
ax = plt.gca()
# Change the aspect ratio
ax.set_aspect(imgratio/ax.get_data_ratio())
# Put y-axis label and numbers at left
ax.get_yaxis().set_label_position('left')
ax.get_yaxis().set_ticks_position('left')
plt.savefig('WARRlinStAmp.pdf',dpi=600)

# Now the hyperbolic
mygpr.showStAmpFig(whichstamp='hyp', saturation=2, yrng=[300,10.94], vrng=[0.01,0.35])
ax = plt.gca()
# Change the aspect ratio
ax.set_aspect(imgratio/ax.get_data_ratio())
# Put label and numbers at bottom
ax.get_xaxis().set_label_position('bottom')
ax.get_xaxis().set_ticks_position('bottom')
plt.savefig('WARRhypStAmp.pdf',dpi=600)


