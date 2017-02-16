import os
import re

class netlist(object):
    def __get_netlist(self,template_name):
        self.__templates_name = template_name
        if self.__templates_name not in self.get_templates_list():
            return "Template missing from templates list"
        else:
            template_path = "{template_path}/{template_name}".format(   template_path = self.__templates_path,
                                                                        template_name = self.__templates_name
            )
            template_file = open ( template_path , 'r+')
            return template_file.read()

    def get_template_variables( self , template_name ):
        netlist = self.__get_netlist(template_name)
        #temp_list = netlist.split('{')
        temp_list = set ( re.findall(r'{\w*',netlist) )
        self.__template_variable_list = map(    lambda variable: str.replace(   variable ,
                                                                                '{',
                                                                                ''
                                                ) ,
                                            temp_list
        )
        return self.__template_variable_list

    def get_templates_list(self):
        temp_list = os.listdir(self.__templates_path)
        return temp_list

    def generate_netlist( self , netlist_path , template_name , netlist_name , values ):
        netlist_template = self.__get_netlist(template_name)
        generated_netlist = netlist_template.format(**values)
        netlist_file_path = "{netlist_path}/{netlist_name}.net".format(     netlist_path = netlist_path,
                                                                            netlist_name = netlist_name
        )
        print netlist_file_path
        #print generated_netlist
        netlist_file = open(netlist_file_path , 'w+')
        netlist_file.write ( generated_netlist )
        pass

    def __init__ ( self , templates_path ) :
        self.__templates_path = templates_path

#-------------------------------------------------------------------------------
def test_main():
    path = "/home/mouse/Documents/ENV/varanda/alpha1/static/hspice"
    netlist_path = '/home/mouse/Documents/ENV/varanda/testDir'

    net = netlist(path)
    invertor =  net.get_templates_list()[0]

    netlist_variables_list =  net.get_template_variables(invertor)

    netlist_values = dict()
    for variable in netlist_variables_list:
        netlist_values[variable] = variable

    net.generate_netlist (  netlist_path = netlist_path ,
                            template_name = invertor ,
                            netlist_name = 'Invertor',
                            values =netlist_values
                            )



if __name__ == '__main__':
    test_main()
