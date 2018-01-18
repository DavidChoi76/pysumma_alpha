#from Decisions import Decisions                        # This is for testing in cmd window.
#from Simulation import Simulation                      # This is for testing in cmd window.
from pysumma.pysumma.Decisions import Decisions       # This is for testing in this python code.
from pysumma.pysumma.Simulation import Simulation     # This is for testing in this python code.

#(2) manipulating file_Manager
##1 Read file_Manager.txt
M_file = Simulation('D:\\pysumma\\summa\\summa_test\\settings_org\\wrrPaperTestCases\\figure09\\summa_fileManager_1dRichards.txt')
#M_file = Simulation('D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\summa_fileManager.txt')

##2 Check the directory and name of files that is controlled by file_Manager.txt
### Case 1 - setting_path that is consisted in filepath and name
setting_path_filepath = M_file.setting_path.filepath
setting_path_value = M_file.setting_path.value
setting_path_name = M_file.setting_path.name
print(setting_path_filepath)
print(setting_path_value)
print(setting_path_name)

### Case 2 - meta_attr that is consisted in filepath, filename, and name
meta_attr_filepath = M_file.meta_attr.filepath
meta_attr_value = M_file.meta_attr.value
meta_attr_name = M_file.meta_attr.name
print(meta_attr_filepath)
print(meta_attr_value)
print(meta_attr_name)

### Case 3 - local_attr that is consisted in filepath, filename, and name
local_attr_filepath = M_file.local_attr.filepath
local_attr_filename = M_file.local_attr.filename
local_attr_value = M_file.local_attr.value
local_attr_name = M_file.local_attr.name
print(local_attr_filepath)
print(local_attr_filename)
print(local_attr_value)
print(local_attr_name)

### Case 4 - decision that is consisted in filepath, filename, and name
decision_filepath = M_file.decision.filepath
decision_filename = M_file.decision.filename
decision_value = M_file.decision.value
decision_name = M_file.decision.name
print(decision_filepath)
print(decision_filename)
print(decision_value)
print(decision_name)


##3 coinciding the Decision file name file_Manager.txt,

##3 Set the parent folder directory that is controlled by file_Manager.txt,
##  you only can change setting_path, input_path, output_path.
##  Below output_path line in file Manager, When you run Execute.py, every lines can recognize their directory according to above directory.

# M_file.setting_path.filepath = "D:\\pysumma\\summa_test\\summa_test\\settings\\"
# M_file.input_path.filepath = "D:\\pysumma\\summa_test\\summa_test\\testCases_data\\inputdata\\fielddata\\reynolds\\"
# M_file.output_path.filepath = "D:\\pysumma\\summa_test\\summa_test\\output\\wrrPaperTestCases\\figure09\\"
# Decisions.
a = M_file.decision
# print(a.filename)
# print(a.filepath)
# print(a.value)
# print(a.name)
a.filename = "choi.txt"
# print(a.filename)
# print(a.value)



