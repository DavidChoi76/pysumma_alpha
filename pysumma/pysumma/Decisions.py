class Decisions:
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
        self.filepath = self.path+self.filename
        self.simulStart = options('simulStart', self.filepath)
        self.simulFinsh = options('simulFinsh', self.filepath)
        self.soilCatTbl = options('soilCatTbl', self.filepath)
        self.vegeParTbl = options('vegeParTbl', self.filepath)
        self.soilStress = options('soilStress', self.filepath)
        self.stomResist = options('stomResist', self.filepath)
        self.num_method = options('num_method', self.filepath)
        self.fDerivMeth = options('fDerivMeth', self.filepath)
        self.LAI_method = options('LAI_method', self.filepath)
        self.f_Richards = options('f_Richards', self.filepath)
        self.groundwatr = options('groundwatr', self.filepath)
        self.hc_profile = options('hc_profile', self.filepath)
        self.bcUpprTdyn = options('bcUpprTdyn', self.filepath)
        self.bcLowrTdyn = options('bcLowrTdyn', self.filepath)
        self.bcUpprSoiH = options('bcUpprSoiH', self.filepath)
        self.bcLowrSoiH = options('bcLowrSoiH', self.filepath)
        self.veg_traits = options('veg_traits', self.filepath)
        self.canopyEmis = options('canopyEmis', self.filepath)
        self.snowIncept = options('snowIncept', self.filepath)
        self.windPrfile = options('windPrfile', self.filepath)
        self.astability = options('astability', self.filepath)
        self.canopySrad = options('canopySrad', self.filepath)
        self.alb_method = options('alb_method', self.filepath)
        self.compaction = options('compaction', self.filepath)
        self.snowLayers = options('snowLayers', self.filepath)
        self.thCondSnow = options('thCondSnow', self.filepath)
        self.thCondSoil = options('thCondSoil', self.filepath)
        self.spatial_gw = options('spatial_gw', self.filepath)
        self.subRouting = options('subRouting', self.filepath)

class options:
    def __init__(self, method, filepath):
        self.text = self.open_read(filepath)
        self.filepath = filepath
        self.method = method
        self.get_description()
        self.options = self.get_option()

    def open_read(self, filepath):
        fileopen = open(filepath, 'rt')
        lines = fileopen.readlines()
        return lines

    def get_default_option(self):
        for line in self.text:
            if line.split()[0] == self.method:
                return line.split()[1].strip()

    def get_default_date_time(self):
        for line in self.text:
            if line.split()[0] == self.method:
                date_time = line.split()[1] +' '+ line.split()[2]
                return date_time

    def get_description(self):
        for line in self.text:
            if line.split()[0] == self.method:
                self.num_and_descrip = line.split('!')[-1]
                self.description = self.num_and_descrip.split(')')[-1].strip()
                number = self.num_and_descrip.find('(')
                self.option_number = self.num_and_descrip[number+1:number+3]
                return self.num_and_descrip

    def get_option(self):
        start_line = 43
        options_list = []
        for num, line in enumerate(self.text[start_line:]):
            line_num = num + start_line
            if line.startswith('! ({})'.format(self.option_number)):
                while self.text[line_num+1].find("---") < 0 and self.text[line_num+1].find("****") < 0:
                    line_num += 1
                    options_list.append(self.text[line_num].split('!')[1].strip())
                else:
                    return options_list

    def wrt_option(self, method, new_option):
        for index, line in enumerate(self.text):
            if line.startswith(method):
                self.text[index] = line.replace(self.option, new_option, 1)
        self.edit_save()

    def wrt_date_time(self, method, new_date_time):
        for index, line in enumerate(self.text):
            if line.startswith(method):
                self.text[index] = line.replace(self.date_time, new_date_time, 1)
        self.edit_save()

    def edit_save(self):
        fileopen = open(self.filepath, 'wt')
        for line in self.text:
            fileopen.write(line)

    @property
    def option(self):
        return self.get_default_option()

    @option.setter
    def option(self, new_option):
        self.wrt_option(self.method, new_option)

    @property
    def date_time(self):
        return self.get_default_date_time()

    @date_time.setter
    def date_time(self, new_date_time):
        self.wrt_date_time(self.method, new_date_time)