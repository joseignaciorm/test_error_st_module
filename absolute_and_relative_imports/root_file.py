from package1 import file1 as pkg1
from package1.subpackage1 import file1 as spkg
from package2 import file1 as pkg2

pkg1.run()

def test():
    print("test")

spkg.subpack_1_file_1()
spkg.run()