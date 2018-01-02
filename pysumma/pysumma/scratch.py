from pysumma.pysumma.Decisions import Decisions

d = Decisions('D:\\pysumma\\pysumma_alpha0\\pysumma\\pysumma\\', 'Decision.txt')

# print(d.Methods)
#
# new_method = 'USGS'
#
# print(d.Methods)
identifier = 'soilCatTbl'

# print(d.Methods(identifier))
print(d.soilCatTbl)


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