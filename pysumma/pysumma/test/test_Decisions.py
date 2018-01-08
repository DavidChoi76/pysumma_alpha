from pysumma.pysumma.Decisions import Decisions
import unittest
from shutil import copyfile

class test_decisions_class(unittest.TestCase):
    filename = 'Decision.txt'
    path = 'D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\test\\'
    file_name2 = 'tmp_{}'.format(filename)
    copyfile('{}{}'.format(path, filename), '{}{}'.format(path, file_name2))
    Decisions_obj = Decisions(path, file_name2)

    def get_value(self, name):
        file_obj = open(self.file_name2, 'r')
        lines = file_obj.readlines()
        file_obj.close()
        for l in lines:
            if l.startswith(name):
                print(l)
                return l.split()[1]


    def test_GetSoilCategoryDataset(self):
        soil_cat_dataset = self.Decisions_obj.soilCatTbl
        self.assertEqual('soilCatTbl', soil_cat_dataset.name)
        self.assertEqual('STAS', soil_cat_dataset.value)
        self.assertEqual(['STAS', 'STAS-RUC', 'ROSETTA'], soil_cat_dataset.options)
        self.assertEqual('soil-category dateset', soil_cat_dataset.description)

    def test_SetSoilCategoryDataset(self):
        soil_cat_dataset = self.Decisions_obj.soilCatTbl
        old = soil_cat_dataset.value
        self.assertEqual(old, 'STAS')
        soil_cat_dataset.value = 'ROSETTA'
        new = soil_cat_dataset.value
        self.assertEqual(new, 'ROSETTA')

    def test_GetGroundwaterParameterization(self):
        ground_para = self.Decisions_obj.groundwatr
        self.assertEqual('groundwatr', ground_para.name)
        self.assertEqual('noXplict', ground_para.value)
        self.assertEqual(['qTopmodl', 'bigBuckt', 'noXplict'], ground_para.options)
        self.assertEqual('choice of groundwater parameterization', ground_para.description)

    def test_SetGroundwaterParameterization(self):
        ground_para = self.Decisions_obj.groundwatr
        old = ground_para.value
        self.assertEqual(old, 'noXplict')
        ground_para.value = 'qTopmodl'
        new = ground_para.value
        self.assertEqual(new, 'qTopmodl')

    def test_GetbcLowrTdynn(self):
        ground_para = self.Decisions_obj.bcLowrTdyn
        self.assertEqual('bcLowrTdyn', ground_para.name)
        self.assertEqual('zeroFlux', ground_para.value)
        self.assertEqual(['presTemp', 'zeroFlux'], ground_para.options)
        self.assertEqual('type of lower boundary condition for thermodynamics', ground_para.description)

    def test_GetbcLowrTdynn(self):
        ground_para = self.Decisions_obj.bcLowrTdyn
        self.assertEqual(self.get_value(ground_para.name), ground_para.value)
        ground_para.value = 'presTemp'
        self.assertEqual('bcLowrTdyn', ground_para.name)
        self.assertEqual(self.get_value(ground_para.name), ground_para.value)
        self.assertEqual(['presTemp', 'zeroFlux'], ground_para.options)
        self.assertEqual('type of lower boundary condition for thermodynamics', ground_para.description)


if __name__ == '__main__':
    unittest.main()