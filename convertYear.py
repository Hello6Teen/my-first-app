import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พุทธศักราช มาเป็น คริสต์ศักราช")

bh_year=st.number_input(" กรอกปี พุทธศักราช  ที่ต้องการแปลง",value=2569)
ce_year=bh_year-543
st.header(f"ปี คริสต์ศักราช คือ : {ce_year}")
