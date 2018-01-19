# pySUMMA

**an Object-Oriented Python wrapper for SUMMA model (Structure for Unifying Multiple Modeling Alternatives)**

## Overview

**pySUMMA is an Object-Oriented Python wrapper for the manipulation, display and
  analysis of SUMMA model**


## Goals

**pySUMMA is intended to provide**

 - Get and set model parameters (working)
 - Run simulations (working)
 - Visualize outputs (working)
 - Automate model calibration or sensitivity studies (working)

## Installation and Usage

**pySUMMA requires Python 3.6 and following packages : **

 - seaborn : statistical data visualization
 - xarray : N-D labeled arrays and datasets in python
 - numpy : the fundamental package for scientific computing with Python
 - matplotlib : a Python 2D plotting library 
 - Cartopy : a library providing cartographic tools.
 - Shapely : a package for creation, manipulation, and analysis of planar geometry    
             objects based on GEOS.
 - geopandas (required numpy, pandas, shapely, fiona, six, pyproj)
 - jupyterthemes
 - Fiona (required gdal) : OGR's neater API
 - pyproj : an interface to the PROJ.4 library for cartographic transformations.
 - GDAL : (Geospatial Data Abstraction Library), a translator library for raster  
           geospatial data formats.

## Examples of installation :

**installation of pysumma**  
**1.)**  open command window and located in pysumma folder same level of setup.py.
```python
>>> D:\pysumma\pysumma_alpha\pysumma\pysumma\pip install .
```

## Examples of unit test :

**running of a unit test using unittest library**  
**1.)**  after installation of pysumma package and located in pysumma folder same level of setup.py.
```python
>>> D:\pysumma\pysumma_alpha\pysumma\pysumma\python setup.py test
```

## Examples of manipulating summa model :

**(1) manipulating Decision text file.**  

**1.)**  import Decisions Module
```python
>>> from pysumma.Decisions import Decisions
```
**2.)**  read Decision text file and create D_file attribute
```python
>>> D_file = Decisions('D:\\pysumma\\summa\\summa_test\\settings_org\\wrrPaperTestCases\\figure09\\summa_zDecisions_1dRichards.txt')  
```
**3.)**  make attribute for (01) simulation start time  
```python
>>> sim_start_time = D_file.simulStart
```
**4.)**  get default simulation start date and time
```python
>>> sim_start_time.value
   "2002-07-01 00:00"
```
**5.)**  set and write simulation start time in Decision text file
```python
>>> sim_start_time.value = "2004-10-01 00:00"
```
**6.)**  make attribute for (02) simulation finish time  
```python
>>> sim_finish_time = D_file.simulFinsh
```
**7.)**  get default simulation finish date and time
```python
>>> sim_finish_time.value
   "2002-07-01 00:00"
```
**8.)**  set and write simulation finish time in Decision text file
```python
>>> sim_finish_time.value = "2005-09-30 00:00"
```
**9.)**  make attribute for (03) soil category dataset  
```python
>>> soil_cat_dataset = D_file.soilCatTbl
```
**10.)**  get abstract method name (first content of each lines)
```python
>>> soil_cat_dataset.name
   "soilCatTbl"
```
**11.)**  get default value in Decision text file  (second content of each lines)
```python
>>> soil_cat_dataset.value
```
**12.)**  get available options for each method
```python
>>> soil_cat_dataset.options
   "['STAS', 'STAS-RUC', 'ROSETTA']"
```
**13.)**  get description of each method
```python
>>> soil_cat_dataset.description
   "soil-category dateset"
```
**14.)**  select option and write selected option in Decision.txt
```python
>>> soil_cat_dataset.value = 'STAR-RUC'
```
**(2) manipulating file Manager file.**  

**1.)**  import Simulation Module
```python
>>> from pysumma.Simulation import Simulation
```
**2.)**  read file Manager text file and create M_file attribute
```python
>>> M_file = Simulation('D:\\pysumma\\summa\\summa_test\\settings_org\\wrrPaperTestCases\\figure09\\summa_fileManager_1dRichards.txt')
```
**3.)**  make filepath attribute for setting_path
```python
>>> setting_path_filepath = M_file.setting_path.filepath
>>> setting_path_filepath
   "/summaTestCases_2.x/settings/"
```
**4.)**  make name attribute for setting_path
```python
>>> setting_path_name = M_file.setting_path.name
>>> setting_path_name
   "setting_path"
```
**5.)**  make filepath attribute for Decision
```python
>>> decision_filepath = M_file.decision.filepath
>>> decision_filepath
   "wrrPaperTestCases/figure09/"
```
**6.)**  make filename attribute for Decision
```python
>>> decision_filename = M_file.decision.filename
>>> decision_filename
   "summa_zDecisions_1dRichards.txt"
```   
**7.)**  make name attribute for Decision
```python
>>> decision_name = M_file.decision.name
>>> decision_name
   "decision"
```   
**8.)**  make change_D_name attribute when users need to change decision file name
```python
>>> change_D_name = M_file.decision
```   
**9.)**  set and change decision file name
```python
>>> change_D_name.filename = "Decision.py"
```   
**(3) Displaying summa output.**  
** Display plot from summa_plot created by andrew bennett from UW ** 

**1.)**  import hovmoller, layers, spatial Module
```python
>>> from pysumma.hovmoller import hovmoller
>>> from pysumma.layers import layers
>>> from pysumma.spatial import spatial
```
**2.)**  read output netcdf file and create attribute.
```python
>>> ds = xr.open_dataset('./pysumma/basinRunoff_2007-2008_distributedTopmodel_1.nc')
```
**3.)**  display output with shapefil using spatial.py
```python
>>> gdf = gp.GeoDataFrame.from_file('./ReynoldsMountainEast.shp')
>>> gdf.plot()
>>> plt.show()
```
**4.)**  display output with shapefil using spatial.py
```python
>>> gdf = gp.GeoDataFrame.from_file('./ReynoldsMountainEast.shp')
>>> gdf.plot()
>>> plt.show()
```
**5.)**  display 2D plot with time or hru and variable using hovmoller.py
```python
>>> hovmoller(ds['scalarSWE'].isel(hru=slice(0,100)), xdim='hru', ydim='dayofyear')
>>> plt.show()
```
**6.)**  display output of variables related layers such as snow and soil using layers.py
```python
>>> ds = xr.open_dataset('./basinRunoff_2007-2008_distributedTopmodel_1.nc').isel(hru=0)
>>> layers(ds.isel(time=slice(0,500)), 'mLayerVolFracWat')
>>> plt.show()
```
**4.)**  display output with shapefil using spatial.py
```python
>>> gdf = gp.GeoDataFrame.from_file('./ReynoldsMountainEast.shp')
>>> gdf.plot()
>>> plt.show()
```

** plotting line plot with variables(1D, 2D)** 

**1.)**  import Plotting Module
```python
>>> from pysumma.Plotting import Plotting
```
**2.)**  assign netCDF file
```python
>>>P_file = Plotting('D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\BasinRunoff_1dRichards.nc')
```
**3.)**  open netCDF file and create plot_info attribute
```python
>>>plot_info = P_file.open_netcdf()
```
**4.)**  Display 1D (time, variable)
```python
variable_1D = [['basin__SurfaceRunoff','2'],['basin__ColumnOutflow','3'], ['basin__AquiferStorage','4'],
			   ['basin__AquiferRecharge', '5'], ['basin__AquiferBaseflow', '6'],['basin__AquiferTranspire','7'],
			   ['averageInstantRunoff', '8'], ['averageRoutedRunoff', '9']]
```
```python
>>>plot_1D = P_file.plot_1d(plot_info, 8)
>>>plt.show()
```
**5.)**  Display 1D (time, hru_num, variable_num_Y)
```python
variable_1D_hru = [['pptrate','0'],['airtemp','1'], ['nSnow','10'], ['nSoil','11'],
                   ['nLayers','12'],['midSoilStartIndex','13'], ['midTotoStartIndex','14'], ['ifcSoilStartIndex','15'],
                   ['ifcTotoStartIndex','16'],['scalarSWE','17'],['scalarSurfaceTemp','23'],['scalarSenHeatTotal','27'],
                   ['scalarLatHeatTotal','28'],['scalarSnowSublimation','29'],['scalarThroughfallSnow','30'],
                   ['scalarThroughfallRain','31'],['scalarRainPlusMelt','32'],['scalarInfiltration','33'],
                   ['scalarExfiltration','34'],['scalarSurfaceRunoff','35']]
```
```python
>>>plot_1D_hru = P_file.plot_1d_hru(plot_info, 0, 17)
>>>plt.show()
```
**6.)**  Display 1D (time, hru_num, variable_num_Y)
```python
>>>plot_1D_hru = P_file.plot_1d_hru(plot_info, 0, 33)
>>>plt.show()
```
**7.)**  Display 1D (time, hru_num, variable_num_Y, layer_time)
```python
variable_1D_layer = [['mLayerTemp','18'],['mLayerVolFracIce','19'], ['mLayerVolFracLiq','20'], ['mLayerVolFracWat','21'],
                   ['mLayerMatricHead','22'],['mLayerDepth','24'], ['mLayerHeight','25'], ['iLayerHeight','26'],
                   ['iLayerLiqFluxSoil','36'],['mLayerLiqFluxSoil','37']]
```
```python
>>>plot_1D_layer = P_file.plot_1d_layer(plot_info, 0, 21, 14)
>>>plt.show()
```
**8.)**  Display 2D (time, hru_num, variable_num_Y, variable_num_X, layer_time)
```python
>>>plot_2D = P_file.plot_2d(plot_info, 0, 21, 25, 14)
>>>plt.show()
```

## Bugs
  Our issue tracker is at https://github.com/DavidChoi76/pysumma_alpha0/issues.
  Please report any bugs that you find.  Or, even better, fork the repository on
  GitHub and create a pull request.  All changes are welcome, big or small, and we
  will help you make the pull request if you are new to git
  (just ask on the issue).

## License
  Distributed with a MIT license; see LICENSE.txt::

  Copyright (C) 2017 pySUMMA Developers
  YoungDon Choi <yc5ef@virginia.edu>