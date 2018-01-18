#from Decisions import Decisions         # This is for testing in cmd window.
from .Decisions import Decisions       # This is for testing in this python code.
class Simulation:
    def __init__(self, filepath):
        self.filepath = filepath
        self.setting_path = file_manager_option('setting_path', self.filepath)
        self.input_path = file_manager_option('input_path', self.filepath)
        self.output_path = file_manager_option('output_path', self.filepath)
        self.decision = file_manager_option('decision', self.filepath)
        self.meta_time = file_manager_option('meta_time', self.filepath)
        self.meta_attr = file_manager_option('meta_attr', self.filepath)
        self.meta_type = file_manager_option('meta_type', self.filepath)
        self.meta_force = file_manager_option('meta_force', self.filepath)
        self.meta_localpar = file_manager_option('meta_localpar', self.filepath)
        self.OUTPUT_CONTROL = file_manager_option('OUTPUT_CONTROL', self.filepath)
        self.meta_index = file_manager_option('meta_index', self.filepath)
        self.meta_basinpar = file_manager_option('meta_basinpar', self.filepath)
        self.meta_basinvar = file_manager_option('meta_basinvar', self.filepath)
        self.local_attr = file_manager_option('local_attr', self.filepath)
        self.local_par = file_manager_option('local_par', self.filepath)
        self.basin_par = file_manager_option('basin_par', self.filepath)
        self.forcing_list = file_manager_option('forcing_list', self.filepath)
        self.initial_cond = file_manager_option('initial_cond', self.filepath)
        self.para_trial = file_manager_option('para_trial', self.filepath)
        self.output_prefix = file_manager_option('output_prefix', self.filepath)
#        self.change = self.decision.value
#        self.decision_obj = self.decision.value.replace("/","\\")
#        self.decision_obj1 = Decisions('D:\\pysumma\\summa_test\\summa_test\\settings\\{}'.format(self.decision_obj))

class file_manager_option:
    def __init__(self, name, filepath):
        self.name = name
        self.file_manager_filepath = filepath

    def open_read(self):
        with open(self.file_manager_filepath, 'rt') as f:
            self.text = f.readlines()
        return self.text

    def get_line_no(self, name):
        text = self.open_read()
        for line_no, line in enumerate(text):
            filepath_filename = line.split("'")
            name1 = filepath_filename[2].split(" ")[-1].strip()
            if name1 == name:
                return line_no, line

    def get_value(self):
        line_no, line = self.get_line_no(self.name)
        words = line.split("'")
        words = [w.strip() for w in words if w.strip() != "" and w.strip() != "!"]
        return words[0]

    def wrt_value(self, new_value):
        line_no, line = self.get_line_no(self.name)
        lines = self.open_read()
        lines[line_no] = line.replace(self.value, new_value, 1)
        self.edit_save(lines)

    def edit_save(self, new_lines):
        with open(self.file_manager_filepath, 'wt') as f:
            f.writelines(new_lines)

    @property
    def value(self):
        return self.get_value()


    @value.setter
    def value(self, new_value):
        self.wrt_value(new_value)

    @property
    def filepath(self):
        if not self.value.endswith('/'):
            return "/".join(self.value.split('/')[:-1]) + "/"
        else:
            return self.value

    @filepath.setter
    def filepath(self, new_value):
        value = new_value + self.filename
        self.wrt_value(value)

    @property
    def filename(self):
        return self.value.split('/')[-1]

    @filename.setter
    def filename(self, new_value):
        value = self.filepath + new_value
        self.wrt_value(value)

