#from package1 import file2 # Absolute import
#from package1.subpackage1 import file1 as spkg
#from package2 import file1 as pkg2

from . import file2
from .subpackage1 import file1 as spkg
from package2 import file1 as pkg2

def pack_1_file_1():
    print("pack_1_file_1")

def run():
    print("running pk1_f1")
    #spkg.subpack_1_file_1()
    #pkg2.pack_2_file_1


file2.pack_2_file_2()