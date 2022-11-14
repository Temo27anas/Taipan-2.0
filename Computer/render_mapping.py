from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Read data from file 'filename.csv'
mapping = pd.read_csv("mapping.csv")
sensorsdata = pd.read_csv("sensorsdata.csv")


#merge the two dataframes based on the time column 
merged = pd.merge(mapping, sensorsdata, on='time')
#eliminate the time column
merged = merged.drop('time', 1)

#create a new dataframe with the data from the merged dataframe
final= pd.DataFrame(columns=['h', 'Sx1', 'Sy1', 'Sx2', 'Sy2', 'Sx3', 'Sy3', 'Sx4', 'Sy4', 'Sx5', 'Sy5', 'Sx6', 'Sy6'])

final['h'] = -1*merged['h']
final['Sx1'] = (6+merged['S1'])*np.cos(0)
final['Sy1'] = (6+merged['S1'])*np.sin(0)
final['Sx2'] = (6+merged['S2'])*np.cos(60 * np.pi / 180)
final['Sy2'] = (6+merged['S2'])*np.sin(60 * np.pi / 180)
final['Sx3'] = (6+merged['S3'])*np.cos(120 * np.pi / 180)
final['Sy3'] = (6+merged['S3'])*np.sin(120 * np.pi / 180)
final['Sx4'] = (6+merged['S4'])*np.cos(180 * np.pi / 180)
final['Sy4'] = (6+merged['S4'])*np.sin(180 * np.pi / 180)
final['Sx5'] = (6+merged['S5'])*np.cos(240 * np.pi / 180)
final['Sy5'] = (6+merged['S5'])*np.sin(240 * np.pi / 180)
final['Sx6'] = (6+merged['S6'])*np.cos(300 * np.pi / 180)
final['Sy6'] = (6+merged['S6'])*np.sin(300 * np.pi / 180)



# Define vertices matrix
v = []
for i in range(0, len(final)):
    v.append([
              (final['Sx1'][i], final['Sy1'][i], final['h'][i]),
              (final['Sx2'][i], final['Sy2'][i], final['h'][i]),
              (final['Sx3'][i], final['Sy3'][i], final['h'][i]),
              (final['Sx4'][i], final['Sy4'][i], final['h'][i]),
              (final['Sx5'][i], final['Sy5'][i], final['h'][i]),
              (final['Sx6'][i], final['Sy6'][i], final['h'][i])])


#print(v)

# Define the vertices that compose each face
f=[]
for i in range(0, len(final)-1):
    f.append([0+6*i, 1+6*i, 1+6*(i+1), 0+6*(i+1)])
    f.append([1+6*i, 2+6*i, 2+6*(i+1), 1+6*(i+1)])
    f.append([2+6*i, 3+6*i, 3+6*(i+1), 2+6*(i+1)])
    f.append([3+6*i, 4+6*i, 4+6*(i+1), 3+6*(i+1)])
    f.append([4+6*i, 5+6*i, 5+6*(i+1), 4+6*(i+1)])
    f.append([5+6*i, 0+6*i, 0+6*(i+1), 5+6*(i+1)])




#print(f)


#Plot vertices
ax.scatter3D([v[i][j][0] for i in range(len(v)) for j in range(len(v[i]))], [v[i][j][1] for i in range(len(v)) for j in range(len(v[i]))], [v[i][j][2] for i in range(len(v)) for j in range(len(v[i]))])

# Plot edges between vertices of each hexagon
for i in range(0, len(v)):
    for j in range(0, len(v[i])):
        ax.plot3D([v[i][j][0], v[i][(j+1)%len(v[i])][0]], [v[i][j][1], v[i][(j+1)%len(v[i])][1]], [v[i][j][2], v[i][(j+1)%len(v[i])][2]], color='black')

# data for 3D scatter plot
vflatten= []
for i in range(0, len(v)):
    for j in range(0, len(v[i])):
        vflatten.append(v[i][j])



plot3d=[]
for i in range(0, len(f)):
    surface=[]
    for j in range(0, 4):
        surface.append(vflatten[f[i][j]])
    plot3d.append(surface)

# Plot faces using coolwarm colormap
ax.add_collection3d(Poly3DCollection(plot3d, facecolors=plt.cm.coolwarm(np.linspace(0, 1, len(plot3d))), linewidths=0.1, edgecolors='k', alpha=0.5))




plt.axis('scaled')

# Set the labels
ax.set_xlabel('X in cm')
ax.set_ylabel('Y in cm')
ax.set_zlabel('Z in cm')


#make to plot axis bigger


#make the z axis longer than the x and y axis





plt.show()
