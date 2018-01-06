from pysumma.pysumma.Decisions import Decisions

D_file = Decisions('D:\\pysumma\\pysumma_alpha0\\pysumma\\pysumma\\', 'Decision.txt')

soil_cat_dataset = D_file.soilCatTbl

print(soil_cat_dataset.method)
print(soil_cat_dataset.option)
print(soil_cat_dataset.options)
print(soil_cat_dataset.num_and_descrip)


soil_cat_dataset.option = 'STAR-RUC'

soil_cat_dataset.option

sim_start_time = D_file.simulStart

print(sim_start_time.date_time)
print(sim_start_time.num_and_descrip)

sim_start_time.date_time = "'2010-11-15 13:00'"

sim_start_time.date_time