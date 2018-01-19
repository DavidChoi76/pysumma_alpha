#from pysumma.Simulation import Simulation # This is for testing in cmd window.
from ..pysumma.Simulation import Simulation # This is for testing in this python code.
import unittest
from shutil import copyfile

class test_simulation_class(unittest.TestCase):

    filename = 'fileManager.txt'
    path = 'D:\\pysumma\\pysumma_alpha\\pysumma\\tests\\'
    filepath = path + filename
    filename2 = 'tmp_{}'.format(filename)
    filepath2 = path + filename2
    copyfile(filepath, filepath2)
    Simulation_obj = Simulation(filepath2)

    def get_value(self, name):
        file_obj = open(self.filepath2, 'r')
        lines = file_obj.readlines()
        file_obj.close()
        for line in lines:
            if line.startswith(name):
                return line.split()[1]

    def test_Getsetting_path(self):
        setting = self.Simulation_obj.setting_path
        self.assertEqual('/home/hydro/summa/summa_test/settings/', setting.filepath)
        self.assertEqual('setting_path', setting.name)

    def test_Setdecision(self):
        decision = self.Simulation_obj.decision
        old = decision.filename
        self.assertEqual(old, self.get_value(decision.name))
        decision.filename = 'Decision.py'
        new = decision.filename
        self.assertEqual(new, 'Decision.py')