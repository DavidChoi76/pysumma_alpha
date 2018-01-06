from pysumma.pysumma.Decisions import Decisions
import unittest
from shutil import copyfile

class test_decisions_class(unittest.TestCase):
    filename = 'Decision.txt'
    path = 'D:\\pysumma\\pysumma_alpha0\\pysumma\\pysumma\\test\\'
    file_name2 = 'tmp_{}'.format(filename)
    copyfile('{}{}'.format(path, filename), '{}{}'.format(path, file_name2))
    Decisionfile = Decisions(path, file_name2)


    def test_GetSoilCategoryDataset(self):
        soil_cat_dataset = self.Decisionfile.soilCatTbl
        self.assertEqual('soilCatTbl', soil_cat_dataset.method)
        self.assertEqual('STAS', soil_cat_dataset.option)
        self.assertEqual(['STAS', 'STAS-RUC', 'ROSETTA'], soil_cat_dataset.options)
        self.assertEqual('soil-category dateset', soil_cat_dataset.description)

    def test_SetSoilCategoryDataset(self):
        soil_cat_dataset = self.Decisionfile.soilCatTbl
        old = soil_cat_dataset.option
        self.assertEqual(old, 'STAS')
        soil_cat_dataset.option = 'ROSETTA'
        new = soil_cat_dataset.option
        self.assertEqual(new, 'ROSETTA')

    def test_GetGroundwaterParameterization(self):
        ground_para = self.Decisionfile.groundwatr
        self.assertEqual('groundwatr', ground_para.method)
        self.assertEqual('noXplict', ground_para.option)
        self.assertEqual(['qTopmodl', 'bigBuckt', 'noXplict'], ground_para.options)
        self.assertEqual('choice of groundwater parameterization', ground_para.description)

    def test_SetGroundwaterParameterization(self):
        ground_para = self.Decisionfile.groundwatr
        old = ground_para.option
        self.assertEqual(old, 'noXplict')
        ground_para.option = 'qTopmodl'
        new = ground_para.option
        self.assertEqual(new, 'qTopmodl')

if __name__ == '__main__':
    unittest.main()