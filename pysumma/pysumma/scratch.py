from pysumma.pysumma.Decisions import Decisions
from pysumma.pysumma.Decisions import file_manager

D_file = Decisions('D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\', 'Decision.txt')
M_file = file_manager('D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\', 'summa_fileManager.txt')

print(M_file)

# sim_start_time = D_file.simulStart
#
# sim_start_time.value
#
# sim_start_time.value = "2013-11-15 11:04"
#
#
# soil_cat_dataset = D_file.soilCatTbl
#
# print(soil_cat_dataset.name)
# print(soil_cat_dataset.value)
# print(soil_cat_dataset.options)
# print(soil_cat_dataset.description)
# #
# # print(D_file.bcLowrTdyn.name)
# # print(D_file.bcLowrTdyn.value)
# # print(D_file.bcLowrTdyn.options)
# # print(D_file.bcLowrTdyn.description)
#
# soil_cat_dataset.value = "STAS"
# # D_file.num_method.value = 'non-iter'
# # D_file.bcLowrTdyn.value = "presTemp"
# # D_file.bcLowrSoiH.value = 'presHead'
#
#
# sim_start_time = D_file.simulStart
# sim_start_time.value = "2013-11-15 11:04"