from pysumma.pysumma.Decisions import Decisions

D_file = Decisions('D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\', 'Decision2.txt')

soil_cat_dataset = D_file.soilCatTbl

print(soil_cat_dataset.name)
print(soil_cat_dataset.value)
print(soil_cat_dataset.options)
print(soil_cat_dataset.description)
# print(soil_cat_dataset.date_time)

D_file.bcLowrTdyn.value = 'choi'
soil_cat_dataset.value = "acaddxaas"
D_file.num_method.value = 'jeff'
D_file.LAI_method.value = 'moh'

print(soil_cat_dataset.value)

sim_start_time = D_file.simulStart
#
print(sim_start_time.value)
#
# sim_start_time.value = "2013-11-15 11:04"
#
# print(sim_start_time.value)