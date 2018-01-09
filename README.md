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

## Examples:

**Intialize using with statement.**  

**1.)**  import Decisions Module

***>>>*** from pysumma.pysumma.Decisions import Decisions

**2.)**  Open and read Decisioin.txt

***>>>*** D_file = Decisions('D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\', 'Decision.txt')  

**3.)**  make attribute for (01) simulation start time  

***>>>*** sim_start_time = D_file.simulStart

**4.)**  get default simulation start date and time

```python
>>> print(sim_start_time.value)
  `2002-07-01 00:00`
 ```

**5.)**  set and write simulation start time in Decision.txt

***>>>*** sim_start_time.value = "2003-07-01 00:00"

**6.)**  make attribute for (03) soil category dataset  

***>>>*** soil_cat_dataset = D_file.soilCatTbl

**7.)**  get abstrat method name (first content of each lines)

***>>>*** print(soil_cat_dataset.name)

  `soilCatTbl`

**8.)**  get default value in Decision.txt  (second content of each lines)

***>>>*** soil_cat_dataset.value

**9.)**  get available options for each method

***>>>*** print(soil_cat_dataset.options)

  `['STAS', 'STAS-RUC', 'ROSETTA']`

**10.)**  get description of each method

***>>>*** print(soil_cat_dataset.description)

  `soil-category dateset`

**11.)**  selected option

***>>>*** soil_cat_dataset.option = 'STAR-RUC'

**12.)**  write selected option in Decision.txt

***>>>*** soil_cat_dataset.option

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
