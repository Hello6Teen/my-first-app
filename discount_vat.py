import streamlit as he
he.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")
price = he.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0 , value=0.0)
discount = he.number_input("กรอกส่วนลด (%):", min_value=0.0 , value=0.0)
he.divider()
vat = price * 0.07
net_price = price - vat
