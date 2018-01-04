class Decisions:
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
        self.filepath = self.path+self.filename
        self.soilCatTbl = option('soilCatTbl', self.filepath)
        self.vegeParTbl = option('vegeParTbl', self.filepath)
        self.soilStress = option('soilStress', self.filepath)
        self.stomResist = option('stomResist', self.filepath)
        self.num_method = option('num_method', self.filepath)
        self.fDerivMeth = option('fDerivMeth', self.filepath)
        self.LAI_method = option('LAI_method', self.filepath)
        self.f_Richards = option('f_Richards', self.filepath)
        self.groundwatr = option('groundwatr', self.filepath)
        self.hc_profile = option('hc_profile', self.filepath)
        self.bcUpprTdyn = option('bcUpprTdyn', self.filepath)
        self.bcLowrTdyn = option('bcLowrTdyn', self.filepath)
        self.bcUpprSoiH = option('bcUpprSoiH', self.filepath)
        self.bcLowrSoiH = option('bcLowrSoiH', self.filepath)
        self.veg_traits = option('veg_traits', self.filepath)
        self.canopyEmis = option('canopyEmis', self.filepath)
        self.snowIncept = option('snowIncept', self.filepath)
        self.windPrfile = option('windPrfile', self.filepath)
        self.astability = option('astability', self.filepath)
        self.canopySrad = option('canopySrad', self.filepath)
        self.alb_method = option('alb_method', self.filepath)
        self.compaction = option('compaction', self.filepath)
        self.snowLayers = option('snowLayers', self.filepath)
        self.thCondSnow = option('thCondSnow', self.filepath)
        self.thCondSoil = option('thCondSoil', self.filepath)
        self.spatial_gw = option('spatial_gw', self.filepath)
        self.subRouting = option('subRouting', self.filepath)

class option:
    def __init__(self, method, filepath):
        self.text = self.open_read(filepath)
        self.filepath = filepath
        self.name = method
        self.get_desc()
        self.options = self.get_option()

    def open_read(self, filepath):
        fileopen = open(filepath, 'rt')
        lines = fileopen.readlines()
        return lines

    def get_attribute(self):
        for line in self.text:
            if line.split()[0] == self.name:
                return line.split()[1].strip()

    def get_desc(self):
        for line in self.text:
            if line.split()[0] == self.name:
                desc_and_number = line.split('!')[-1]
                self.description = desc_and_number.split(')')[-1].strip()
                parenth_idx = desc_and_number.find('(')
                self.option_number = desc_and_number[parenth_idx+1:parenth_idx+3]
                return line.split('!')[-1]

    def get_option(self):
        dec = self.description
        start_line = 43
        options_list = []
        for num, line in enumerate(self.text[start_line:]):
            line_no = num + start_line
            if line.startswith('! ({})'.format(self.option_number)):
                while self.text[line_no+1].find("---") < 0 and self.text[line_no+1].find("****") < 0:
                    line_no += 1
                    options_list.append(self.text[line_no].split('!')[1].strip())
                else:
                    return options_list

    def wrt_attribute(self, method, selection):
        for index, line in enumerate(self.text):
            if line.startswith(method):
                self.text[index] = line.replace(self.value, selection, 1)
        self.edit_save()

    def edit_save(self):
        fileopen = open(self.filepath, 'wt')
        for line in self.text:
            fileopen.write(line)

    @property
    def value(self):
        return self.get_attribute()

    @value.setter
    def value(self, new_value):
        self.wrt_attribute(self.name, new_value)