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
        self.assertEqual('STAS', soil_cat_dataset.value)
        self.assertEqual('soilCatTbl', soil_cat_dataset.name)
        self.assertEqual('soil-category dateset', soil_cat_dataset.description)
        self.assertEqual(['STAS', 'STAS-RUC', 'ROSETTA'], soil_cat_dataset.options)

    def test_SetSoilCategoryDataset(self):
        soil_cat_dataset = self.Decisionfile.soilCatTbl
        old = soil_cat_dataset.value
        self.assertEqual(old, 'STAS')
        soil_cat_dataset.value = 'ROSETTA'
        new = soil_cat_dataset.value
        self.assertEqual(new, 'ROSETTA')

if __name__ == '__main__':
    unittest.main()