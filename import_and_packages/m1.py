import m2
from m2 import output_m2_1
from package1 import file1
from package1.file2 import pack_2_file_2
from package1.subpackage1 import subfile1 # absolute import
import streamlit as st

output_m2_1()
file1.pack_1_file_1()
subfile1.subpack_1_file_1()
pack_2_file_2()

if st.checkbox("Bigquery Connection"):
    st.subheader("Markdown information to set template")

    if st.button("Send"):
        subfile1.subpack_1_file_1()


