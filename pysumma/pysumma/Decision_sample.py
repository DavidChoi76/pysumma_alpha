#from Decisions import Decisions                        # This is for testing in cmd window.
from pysumma.pysumma.Decisions import Decisions       # This is for testing in this python code.

#(1) manipulating Decisions.py
##1 Read Decision.txt and create D_file attribute

D_file = Decisions('D:\\pysumma\\summa\\summa_test\\settings_org\\wrrPaperTestCases\\figure09\\summa_zDecisions_1dRichards.txt')

##2 Read and change simlulation start time
sim_start_time = D_file.simulStart
print(sim_start_time.name)
print(sim_start_time.value)
print(sim_start_time.description)
sim_start_time.value = "2004-10-01 00:00"

##3 Read and change simlulation finish time
sim_finish_time = D_file.simulFinsh
print(sim_finish_time.name)
print(sim_finish_time.value)
print(sim_finish_time.description)
sim_finish_time.value = "2005-09-30 00:00"

##3 Read and change calculation methods
### Case 1 - (03) soil-category dateset
soil_cat_dataset = D_file.soilCatTbl
print(soil_cat_dataset.name)
print(soil_cat_dataset.value)
print(soil_cat_dataset.options)
print(soil_cat_dataset.description)
soil_cat_dataset.value = "ROSETTA"

### Case 2 - (07) choice of numerical method
numerical_method = D_file.num_method
print(numerical_method.name)
print(numerical_method.value)
print(numerical_method.options)
print(numerical_method.description)
numerical_method.value = "itersurf"

### Case 3 - (14) type of lower boundary condition for thermodynamics
low_boun_therm = D_file.bcLowrTdyn
print(low_boun_therm.name)
print(low_boun_therm.value)
print(low_boun_therm.options)
print(low_boun_therm.description)
low_boun_therm.value = "presTemp"

### Case 4 - (22) choice of canopy shortwave radiation method
can_shrwa_radi = D_file.canopySrad
print(can_shrwa_radi.name)
print(can_shrwa_radi.value)
print(can_shrwa_radi.options)
print(can_shrwa_radi.description)
can_shrwa_radi.value = "noah_mp"


