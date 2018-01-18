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
D:\pysumma\pysumma_alpha\pysumma\pysumma\pip install .
```

## Examples of unit test :

**running of a unit test using unittest library**  
**1.)**  after installation of pysumma package and located in pysumma folder same level of setup.py.
```python
D:\pysumma\pysumma_alpha\pysumma\pysumma\python setup.py test
```

## Examples of manipulating summa model :

**Intialize using with statement.**  

**1.)**  import Decisions Module
```python
>>> from pysumma.pysumma.Decisions import Decisions
```
**2.)**  Open and read Decision.txt
```python
>>> D_file = Decisions('D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\', 'Decision.txt')  
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
**5.)**  set and write simulation start time in Decision.txt
```python
>>> sim_start_time.value = "2003-07-01 00:00"
```
**6.)**  make attribute for (03) soil category dataset  
```python
>>> soil_cat_dataset = D_file.soilCatTbl
```
**7.)**  get abstract method name (first content of each lines)
```python
>>> print(soil_cat_dataset.name)
   "soilCatTbl"
```
**8.)**  get default value in Decision.txt  (second content of each lines)
```python
>>> soil_cat_dataset.value
```
**9.)**  get available options for each method
```python
>>> print(soil_cat_dataset.options)
   "['STAS', 'STAS-RUC', 'ROSETTA']"
```
**10.)**  get description of each method
```python
>>> print(soil_cat_dataset.description)
   "soil-category dateset"
```
**11.)**  select option and write selected option in Decision.txt
```python
>>> soil_cat_dataset.value = 'STAR-RUC'
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
