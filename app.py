from import_and_packages import m2
from import_and_packages.package1 import file1
from import_and_packages.package1.file2 import pack_2_file_2
from import_and_packages.package1.subpackage1 import subfile1 # absolute import
import streamlit as st

m2.output_m2_1()
file1.pack_1_file_1()
subfile1.subpack_1_file_1()
pack_2_file_2()

if st.checkbox("Bigquery Connection"):
    st.subheader("Markdown information to set template")

    if st.button("Send"):
        res = subfile1.subpack_1_file_1()
        st.warning(f"{subfile1.subpack_1_file_1()}")


