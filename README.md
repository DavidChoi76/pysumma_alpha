pySUMMA
======

*Python Wrapper for SUMMA(Structure for Unifying Multiple Modeling Alternatives)

Overview
--------

pySUMMA is a Python language software package for the manipulation, display and
analysis of SUMMA


Goals
-----
pySUMMA is intended to provide

- Get and set model parameters (working)
- Run simulations (working)
- Visualize outputs (working)
- Automate model calibration or sensitivity studies (working)

Examples:

Intialize using with statement.  

>>> # import Decisions Module
>>> from pysumma.pysumma.Decisions import Decisions
>>> # Open and read Decisioin.txt
>>> D_file = Decisions('D:\\pysumma\\pysumma_alpha0\\pysumma\\pysumma\\', 'Decision.txt')    
>>> # make attribute for (3) soil category dataset  
>>> soil_cat_dataset = D_file.soilCatTbl
>>> # get abstrat method name (first content of each lines)
>>> soil_cat_dataset.method
>>> # get default option in Decision.txt  (second content of each lines)
>>> soil_cat_dataset.option
>>> # get available options for each method
>>> soil_cat_dataset.options
>>> # get description(full_name) of each method
>>> soil_cat_dataset.num_and_descrip
>>> # selected option
>>> soil_cat_dataset.option = 'STAR-RUC'
>>> # write selected option in Decision.txt
>>> soil_cat_dataset.option

Bugs
----

Our issue tracker is at https://github.com/DavidChoi76/pysumma_alpha0/issues.
Please report any bugs that you find.  Or, even better, fork the repository on
GitHub and create a pull request.  All changes are welcome, big or small, and we
will help you make the pull request if you are new to git
(just ask on the issue).

License
-------

Distributed with a MIT license; see LICENSE.txt::

   Copyright (C) 2017 pySUMMA Developers
   YoungDon Choi <yc5ef@virginia.edu>
