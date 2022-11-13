import plotly.graph_objects as go
import numpy as np
import pandas as pd

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


# Create figure
fig = go.Figure()

# Define the vertices that compose each face
f=[]
for i in range(0, len(final)-1):
    f.append([0+6*i, 1+6*i, 1+6*(i+1), 0+6*(i+1)])
    f.append([1+6*i, 2+6*i, 2+6*(i+1), 1+6*(i+1)])
    f.append([2+6*i, 3+6*i, 3+6*(i+1), 2+6*(i+1)])
    f.append([3+6*i, 4+6*i, 4+6*(i+1), 3+6*(i+1)])
    f.append([4+6*i, 5+6*i, 5+6*(i+1), 4+6*(i+1)])
    f.append([5+6*i, 0+6*i, 0+6*(i+1), 5+6*(i+1)])




#plot points

fig.add_trace(go.Scatter3d(x=final['Sx1'], y=final['Sy1'], z=final['h'], mode='markers', marker=dict(size=2, color='red', opacity=0.8)))
fig.add_trace(go.Scatter3d(x=final['Sx2'], y=final['Sy2'], z=final['h'], mode='markers', marker=dict(size=2, color='red', opacity=0.8)))
fig.add_trace(go.Scatter3d(x=final['Sx3'], y=final['Sy3'], z=final['h'], mode='markers', marker=dict(size=2, color='red', opacity=0.8)))
fig.add_trace(go.Scatter3d(x=final['Sx4'], y=final['Sy4'], z=final['h'], mode='markers', marker=dict(size=2, color='red', opacity=0.8)))
fig.add_trace(go.Scatter3d(x=final['Sx5'], y=final['Sy5'], z=final['h'], mode='markers', marker=dict(size=2, color='red', opacity=0.8)))
fig.add_trace(go.Scatter3d(x=final['Sx6'], y=final['Sy6'], z=final['h'], mode='markers', marker=dict(size=2, color='red', opacity=0.8)))

#link the points for each hexagon to create parallel hexagons
# for i in range(0, len(final)):
#     fig.add_trace(go.Scatter3d(x=[final['Sx1'][i], final['Sx2'][i]], y=[final['Sy1'][i], final['Sy2'][i]], z=[final['h'][i], final['h'][i]], mode='lines', line=dict(color='blue', width=1)))
#     fig.add_trace(go.Scatter3d(x=[final['Sx2'][i], final['Sx3'][i]], y=[final['Sy2'][i], final['Sy3'][i]], z=[final['h'][i], final['h'][i]], mode='lines', line=dict(color='blue', width=1)))
#     fig.add_trace(go.Scatter3d(x=[final['Sx3'][i], final['Sx4'][i]], y=[final['Sy3'][i], final['Sy4'][i]], z=[final['h'][i], final['h'][i]], mode='lines', line=dict(color='blue', width=1)))
#     fig.add_trace(go.Scatter3d(x=[final['Sx4'][i], final['Sx5'][i]], y=[final['Sy4'][i], final['Sy5'][i]], z=[final['h'][i], final['h'][i]], mode='lines', line=dict(color='blue', width=1)))
#     fig.add_trace(go.Scatter3d(x=[final['Sx5'][i], final['Sx6'][i]], y=[final['Sy5'][i], final['Sy6'][i]], z=[final['h'][i], final['h'][i]], mode='lines', line=dict(color='blue', width=1)))
#     fig.add_trace(go.Scatter3d(x=[final['Sx6'][i], final['Sx1'][i]], y=[final['Sy6'][i], final['Sy1'][i]], z=[final['h'][i], final['h'][i]], mode='lines', line=dict(color='blue', width=1)))




    
fig.show()