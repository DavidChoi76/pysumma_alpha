# pySUMMA

**an Object-Oriented Python wrapper for SUMMA model (Structure for Unifying Multiple Modeling Alternatives)**

## Overview

**pySUMMA is an Object-Oriented Python wrapper for the manipulation, display and
  analysis of SUMMA model**


## Goals

**pySUMMA is intended to provide**

 - Get and set model parameters (in progress)
 - Run simulations (in progress)
 - Visualize outputs (in progress)
 - Automate model calibration or sensitivity studies (in progress)

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
 
 - VirtualBox
                 

## Download pysumma_alpha and summa_testcase :

**1.)**  open VirtualBox (check whether summa image or not
**2.)**  open LXTerminal
**3.)**  move to Downloads folder and download pysumma_alpha
```python
>>> git clone http://github.com/DavidChoi76/pysumma_alpha
```
**4.)**  open web browser(https://ral.ucar.edu/projects/summa) and download summa_testcase(summaTestCases_2x.tar.gz)       
           

## Examples of installation :

**installation of pysumma**  
**1.)**  move into pysumma folder same level of setup.py.
```python
>>> ~/Downloads/pysumma_alpha/pysumma/pysumma/pip install .
```

## Examples of unit test :

**a unit test using unittest library**  

```python
>>> ~/Downloads/pysumma_alpha/pysumma/pysumma/python setup.py test
```

## Examples of manipulating summa model :

**(1) manipulating Decision text file.**  

**1.)**  import Decisions Module
```python
>>> from pysumma.Decisions import Decisions
```
**2.)**  read Decision text file and create D attribute
```python
>>> D = Decisions('/home/hydro/Downloads/summaTestCases_2.x/settings/wrrPaperTestCases/figure01/summa_zDecisions_riparianAspenCLM2stream.txt')
```
**3.)**  make attribute for (01) simulation start time  
```python
>>> sim_start_time = D.simulStart
```
**4.)**  get default simulation start date and time
```python
>>> sim_start_time.value
   "2005-07-01 00:00"
```
**5.)**  set and write simulation start time in Decision text file
```python
>>> sim_start_time.value = "2006-07-01 00:00"
```
**6.)**  make attribute for (02) simulation finish time  
```python
>>> sim_finish_time = D_file.simulFinsh
```
**7.)**  get default simulation finish date and time
```python
>>> sim_finish_time.value
   "2008-09-30 00:00"
```
**8.)**  set and write simulation finish time in Decision text file
```python
>>> sim_finish_time.value = "2007-09-30 00:00"
```
**9.)**  make attribute for (03) soil category dataset  
```python
>>> soil_cat_dataset = D.soilCatTbl
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
**2.)**  read file Manager text file and create S attribute
```python
>>> S = Simulation('/home/hydro/Downloads/summaTestCases_2.x/settings/wrrPaperTestCases/figure01/summa_fileManager_riparianAspenCLM2stream.txt')
```
**3.)**  make attribute of setting_path
```python
>>> setting_path = S.setting_path
>>> setting_path.filepath
   "/summaTestCases_2.x/settings/"
>>> setting_path_name
   "setting_path" 
```
**4.)**  make attribute of Decision
```python
>>> decision = S.decision_path
>>> decision.filepath
   "wrrPaperTestCases/figure09/"
>>> decision.filename
   "summa_zDecisions_riparianAspenCLM2stream.txt"
>>> decision.name
   "decision"
```   
**5.)**  change decision file name when users need to change decision file name
```python
>>> decision.filename = "Decision.py"
```   

**(3) running summa model.**  

**1.)**  create attribute and set summa executable file
```python
>>> S.executable = "/home/hydro/Downloads/summa-master/bin/summa.exe"
```
**2.)**  assign suffix for output filename
```python
>>> S.run_suffix = "pysumma_demo"
```
**3.)**  run summa
```python
>>> S.execute()
```

**(4) Displaying summa output.**  

** plotting line plot with variables(1D, 2D)** 

**1.)**  import Plotting Module
```python
>>> from pysumma.Plotting import Plotting
```
**2.)**  read netCDF file
```python
>>>P = Plotting('/home/hydro/Downloads/summaTestCases_2.x/output/wrrPaperTestCases/figure01/vegImpactsRad_2006-2007_pysumma_demo_1.nc').open_netcdf()
```
**3.)**  open and read netCDF file and create plot_info attribute
```python
>>>P_info = P.open_netcdf()
```
**4.)**  Display 1D (time, variable)
```python
variable = [['basin__SurfaceRunoff','2'],['basin__ColumnOutflow','3'], 
            ['basin__AquiferStorage','4'],['basin__AquiferRecharge', '5'], 
            ['basin__AquiferBaseflow', '6'],['basin__AquiferTranspire','7'],
			['averageInstantRunoff', '8'], ['averageRoutedRunoff', '9']]
```
```python
>>>P.plot_1d(P_info, 5)
```
**5.)**  Display 1D (time, hru_num, variable_num_Y)
```python
variable_num_Y = [['pptrate','0'],['airtemp','1'], ['nSnow','10'], ['nSoil','11'],
                  ['nLayers','12'],['midSoilStartIndex','13'], ['midTotoStartIndex','14'], 
                  ['ifcSoilStartIndex','15'],['ifcTotoStartIndex','16'],['scalarSWE','17'],
                  ['scalarSurfaceTemp','23'],['scalarSenHeatTotal','27'],
                  ['scalarLatHeatTotal','28'],['scalarSnowSublimation','29'],
                  ['scalarThroughfallSnow','30'],['scalarThroughfallRain','31'],
                  ['scalarRainPlusMelt','32'],['scalarInfiltration','33'],
                  ['scalarExfiltration','34'],['scalarSurfaceRunoff','35']]
```
```python
>>>P.plot_1d_hru(P_info, 0, 17)
```
**6.)**  Display 1D (time, hru_num, variable_num_Y, layer_time)
```python
variable_num_Y = [['mLayerTemp','18'],['mLayerVolFracIce','19'], ['mLayerVolFracLiq','20'], 
                  ['mLayerVolFracWat','21'],['mLayerMatricHead','22'],['mLayerDepth','24'], 
                  ['mLayerHeight','25'], ['iLayerHeight','26'],['iLayerLiqFluxSoil','36'],
                  ['mLayerLiqFluxSoil','37']]
layer_time = [['midSoilStartIndex','13'], ['midTotoStartIndex','14'], 
              ['ifcSoilStartIndex','15'], ['ifcTotoStartIndex','16']]             
```
```python
>>>P.plot_1d_layer(P_info, 0, 26, 14)
```

** Display plot from summa_plot created by andrew bennett from UW ** 

**1.)**  import layers
```python
>>> from pysumma.layers import layers
>>> import xarray as xr
>>> import geopandas as gp
```
**2.)**  display output of variables related layers such as snow and soil using layers.py
```python
>>> ds = xr.open_dataset('/home/hydro/Downloads/summaTestCases_2.x/output/wrrPaperTestCases/figure01/vegImpactsRad_2006-2007_pysumma_demo_1.nc').isel(hru=0)
>>> layers(ds.isel(time=slice(0,500)), 'mLayerVolFracWat')
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