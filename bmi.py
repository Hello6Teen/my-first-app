import streamlit as sx

sx.markdown("# :orange[🏋️‍♂️ คำนวณดัชนีมวลกาย ]")
sx.write(" กรุณากรอกน้ำหนักและส่วนสูงของคุณ เพื่อเป็นการตรวจสอบเบื้องต้น ")

weight = sx.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value = 1.0, value = 1.0)
height_cm = sx.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value = 1.0, value = 1.0)

if sx.button("คำนวณค่า BMI🎯"):
  height_m = height_cm / 100
  bmi = weight / (height_m ** 2)

  sx.write("---")
  sx.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

if bmi < 18.5:
  sx.warning("⚠️ คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
elif 18.5 <= bmi <= 22.9:
  sx.success("🍏 คุณมีน้ำหนักอยู่ในเกณฑ์ (พอดี)")
elif 23.0 <= bmi <= 25.0:
  sx.info("💡 คุณมีน้ำหนักเกินเกณฑ์ (ท้วม)")
else:
  st.error("❗ คุณมีน้ำหนักมากกว่าเกณฑ์ (อ้วน)")

sx.divider()
sx.write("นาย จารุวิทย์ จีปวน เลขที่ 36  ม.4/5")
