from pysumma.pysumma.Decisions import Decisions
from pysumma.pysumma.Methods import Methods, Selections, Descriptions

D_file = Decisions('D:\\pysumma\\pysumma_alpha0\\pysumma\\pysumma\\', 'Decision.txt')

print(Methods[0], Selections[0], Descriptions[0])

method = Methods[0]
selection = Selections[0][2]
description = Descriptions[0]

#print(method.split()[0])
Selection = Selections[0][2]

print(D_file.get_attribute(method))
D_file.wrt_attribute(method, Selection)






# print(d.Methods)
#
# new_method = 'USGS'
#
# print(d.Methods)
#identifier = 'soilCatTbl'
#3
# print(d.Methods(identifier))
#print(d.soilCatTbl)


#
# print(d.Methods(self, identifier))
#
# new_method = 'USGS'
#
# #
# #d.soilCatTbl = 'ROSETTA'
# #
# print(d.Methods(identifier))


# @property
# def Methods(self, identifier):
#     return self.get_attribute(identifier)
#
#
# @Methods.setter
# def soilCatTbl(self, identifier, new_method):
#     self.wrt_attribute(identifier, new_method)