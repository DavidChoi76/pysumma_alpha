from pysumma.pysumma.Plotting import Plotting
from pysumma.pysumma.hovmoller import hovmoller
from pysumma.pysumma.layers import layers
from pysumma.pysumma.spatial import spatial

#(4) Display Plotting.py
##1 Display plot from summa_plot created by andrew bennett from UW
import pandas as pd
import xarray as xr
import geopandas as gp
import pandas
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
#jtplot.style('gruvboxd')
jtplot.figsize(x=10,y=10)

### Case 1 - Read output netcdf file and create attribute.
ds = xr.open_dataset('./basinRunoff_2007-2008_distributedTopmodel_1.nc')

### Case 2 - using spatial.py to display output with shapefile.
gdf = gp.GeoDataFrame.from_file('./ReynoldsMountainEast.shp')
gdf.plot()
plt.show()

### Case 3 - using hovmoller.py to display 2D plot with time or hru and variable.
hovmoller(ds['scalarSWE'].isel(hru=slice(0,100)), xdim='hru', ydim='dayofyear')
plt.show()

### Case 4 - using layers.py to display output of variables related layers such as snow and soil.
ds = xr.open_dataset('./basinRunoff_2007-2008_distributedTopmodel_1.nc').isel(hru=0)
layers(ds.isel(time=slice(0,500)), 'mLayerVolFracWat')
plt.show()

##2 plotting line curve with variables(1D, 2D)
import seaborn as sns
import xarray as xr
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

P_file = Plotting('D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\BasinRunoff_1dRichards.nc')

plot_info = P_file.open_netcdf()
# Attribute = dict(Text_Info.attrs)
# Dimensions = Text_Info.dims
# Data_variables = Text_Info.data_vars

plot_1D = P_file.plot_1d(plot_info, 8)
plt.show()

plot_1D_hru = P_file.plot_1d_hru(plot_info, 0, 17)
plt.show()

plot_1D_hru = P_file.plot_1d_hru(plot_info, 0, 33)
plt.show()

plot_1D_layer = P_file.plot_1d_layer(plot_info, 0, 21, 14)
plt.show()

plot_2D = P_file.plot_2d(plot_info, 0, 21, 25, 14)
plt.show()