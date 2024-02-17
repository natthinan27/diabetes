import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
import matplotlib.gridspec as gridspec


html_1 = """
<div style="background-color:#E799A3;margin-top:40px;padding:5px;border-radius:5px;border-bottom: 3px solid #31333F;border-top: 3px solid #31333F;">
<center><h4>การวิเคราะห์และการทำนายความเสี่ยงผู้ป่วยเป็นโรคเบาหวานที่ผู้ป่วยเป็นผู้หญิง</h4><h5>Analysis and prediction of the risk of diabetes in female patients.</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    st.write("") 

with col2:
    st.image("./pic/home.jpg")

with col3:
    st.write("")

### Visualization ###

df = pd.read_excel('./data/diabetes.xlsx')


### Analysis ###

html_6 = """
<div style="background-color:#87A5E0;border-bottom: 3px solid #31333F;border-top: 3px solid #31333F;">
<center><h3>Example data table</h3></center>
</div>
"""
st.markdown(html_6, unsafe_allow_html=True)
st.markdown("")
st.write(df.head(10))

html_7 = """
<div style="background-color:#87A5E0;border-bottom: 3px solid #31333F;border-top: 3px solid #31333F;margin-top:20px;">
<center><h3>Class Prediction</h3></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")


# Your existing code
s1 = st.number_input("# Pregnancies : จำนวนการตั้งครรภ์")
s2 = st.number_input("# Glucose : ระดับกลูโคสในเลือด")
s3 = st.number_input("# BloodPressure : การวัดความดันโลหิต")
s4 = st.number_input("# SkinThickness : ความหนาของผิวหนัง")
s5 = st.number_input("# Insulin : ระดับอินซูลินในเลือด")
s6 = st.number_input("# BMI : ดัชนีมวลกาย")
s7 = st.number_input("# DiabetesPedigreeFunction : เปอร์เซ็นต์โรคเบาหวาน")
s8 = st.number_input("# Age : อายุของผู้ป่วย")
s9 = st.selectbox("# Outcome : ผลลัพธ์สุดท้าย  (1 = ใช่ 0 = ไม่ใช่)", [0, 1])

# Adjusting font size and making it bold
st.markdown("<style>h1{font-size: 18px !important;}</style>", unsafe_allow_html=True)
st.markdown("<style>label{font-size: 16px !important; font-weight: bold;}</style>", unsafe_allow_html=True)

if st.button("ทำนายผล"):

   X=df.drop(["Outcome"],axis=1)
   y=df["Outcome"]

   rf_model = RandomForestClassifier()  # สร้างโมเดล Random Forests
   rf_model.fit(X, y)



   x_input = np.array([[s1, s2, s3, s4, s5, s6, s7, s8, s9]])

   out = rf_model.predict(x_input)

   if out[0]== 0 :
          
      html_8 = """
      <div style="background-color:#ffffff;padding:20px;border: 3px solid #31333F;">
      <center><h3 style="border-bottom: 3px solid #31333F;">โอกาสหัวใจวายน้อย</h3></center>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">โรคหัวใจวาย (Coronary Artery Disease, CAD) เป็นภาวะที่เกิดจากการสะสมของเส้นเลือดในหัวใจ (หลอดเลือดในหัวใจ) ทำให้การไหลของเลือดที่จำเป็นสำหรับการให้สารอาหารและออกซิเจนให้กับกล้ามเนื้อหัวใจลดลง สาเหตุหลักของโรคหัวใจวายคือการสะสมของตะกอนไขมันและแร่ธาตุในเส้นเลือดในหัวใจ (เช่น เนื้อเยื่อไขมัน, เซลล์เลือดขาว, และแคลเซียม) ซึ่งทำให้เกิดลิ่ม (plaque) ในเส้นเลือด ลิ่มนี้จะทำให้เส้นเลือดตีบ และสามารถทำให้เกิดอาการหัวใจวาย นี่คือบางวิธีที่อาจช่วยลดโอกาสหัวใจวาย</h6></left>
      <ul>
         <li>รับประทานอาหารที่สุขภาพดี:การบริโภคอาหารที่รวมถึงผัก, ผลไม้, และอาหารที่มีไขมันไม่เบาหรือไขมันดีสามารถช่วยลดความเสี่ยง</li>
         <li>ออกกำลังกาย:การมีกิจกรรมทางกายเป็นประจำ อย่างน้อย 150 นาทีต่อสัปดาห์ เช่น เดินเร็ว, วิ่ง, หรือว่ายน้ำ</li>
         <li>ควบคุมน้ำหนัก:การรักษาน้ำหนักที่เหมาะสมสามารถช่วยลดโอกาสหัวใจวาย</li>
         <li>การเลิกสูบบุหรี่:การเลิกสูบบุหรี่จะช่วยลดความเสี่ยงของโรคหัวใจวาย</li>
         <li>ควบคุมและรักษาโรคประจำตัว:การควบคุมโรคเบาหวาน, ความดันโลหิต, และโรคอื่น ๆ ที่เป็นปัจจัยเสี่ยง</li>
         <li>การบริหารจัดการสเตรส:การใช้เทคนิคการบริหารจัดการสเตรส เช่น การฝึกสมาธิหรือการทำโยคะ</li>
         <li>การดื่มแอลกอฮอล์อย่างมีสติ:การดื่มแอลกอฮอล์ในปริมาณที่ปลอดภัยมีผลต่อการลดความเสี่ยง</li>
         <li>การตรวจสุขภาพประจำปี:การตรวจสุขภาพประจำปีเพื่อตรวจสอบสุขภาพโดยรวมและความเสี่ยงต่อโรค</li>
         <li>การนอนหลับเพียงพอ:การนอนหลับประจำวันในปริมาณที่เหมาะสมสามารถส่งเสริมสุขภาพหัวใจ</li>
         <li>การหลีกเลี่ยงการบริโภคอาหารที่มีสารอาหารไม่ดี:ลดการบริโภคอาหารที่มีโคเลสเตอรอลสูง, น้ำตาล, และเกลือ</li>
      </ul>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">การปฏิบัติตนตามแนวทางดังกล่าวจะช่วยลดโอกาสที่จะเป็นโรคหัวใจวายและส่งเสริมสุขภาพหัวใจที่แข็งแรง. อย่าลืมปรึกษาแพทย์หากคุณมีปัญหาสุขภาพหรือต้องการคำแนะนำเพิ่มเติมเกี่ยวกับการรักษาและป้องกันโรคหัวใจวาย</h6></left>
      </div>
      """
      st.markdown(html_8, unsafe_allow_html=True)
      st.markdown("")

   elif out[0]==1: 
          
      html_9 = """
      <div style="background-color:#ffffff;padding:20px;border: 3px solid #31333F;">
      <center><h3 style="border-bottom: 3px solid #31333F;">โอกาสหัวใจวายมาก</h3></center>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">โรคหัวใจวาย (Coronary Artery Disease, CAD) เป็นภาวะที่เกิดจากการสะสมของเส้นเลือดในหัวใจ (หลอดเลือดในหัวใจ) ทำให้การไหลของเลือดที่จำเป็นสำหรับการให้สารอาหารและออกซิเจนให้กับกล้ามเนื้อหัวใจลดลง สาเหตุหลักของโรคหัวใจวายคือการสะสมของตะกอนไขมันและแร่ธาตุในเส้นเลือดในหัวใจ (เช่น เนื้อเยื่อไขมัน, เซลล์เลือดขาว, และแคลเซียม) ซึ่งทำให้เกิดลิ่ม (plaque) ในเส้นเลือด ลิ่มนี้จะทำให้เส้นเลือดตีบ และสามารถทำให้เกิดอาการหัวใจวาย นี่คือบางวิธีที่อาจช่วยลดโอกาสหัวใจวาย</h6></left>
      <ul>
         <li>รับประทานอาหารที่สุขภาพดี:การบริโภคอาหารที่รวมถึงผัก, ผลไม้, และอาหารที่มีไขมันไม่เบาหรือไขมันดีสามารถช่วยลดความเสี่ยง</li>
         <li>ออกกำลังกาย:การมีกิจกรรมทางกายเป็นประจำ อย่างน้อย 150 นาทีต่อสัปดาห์ เช่น เดินเร็ว, วิ่ง, หรือว่ายน้ำ</li>
         <li>ควบคุมน้ำหนัก:การรักษาน้ำหนักที่เหมาะสมสามารถช่วยลดโอกาสหัวใจวาย</li>
         <li>การเลิกสูบบุหรี่:การเลิกสูบบุหรี่จะช่วยลดความเสี่ยงของโรคหัวใจวาย</li>
         <li>ควบคุมและรักษาโรคประจำตัว:การควบคุมโรคเบาหวาน, ความดันโลหิต, และโรคอื่น ๆ ที่เป็นปัจจัยเสี่ยง</li>
         <li>การบริหารจัดการสเตรส:การใช้เทคนิคการบริหารจัดการสเตรส เช่น การฝึกสมาธิหรือการทำโยคะ</li>
         <li>การดื่มแอลกอฮอล์อย่างมีสติ:การดื่มแอลกอฮอล์ในปริมาณที่ปลอดภัยมีผลต่อการลดความเสี่ยง</li>
         <li>การตรวจสุขภาพประจำปี:การตรวจสุขภาพประจำปีเพื่อตรวจสอบสุขภาพโดยรวมและความเสี่ยงต่อโรค</li>
         <li>การนอนหลับเพียงพอ:การนอนหลับประจำวันในปริมาณที่เหมาะสมสามารถส่งเสริมสุขภาพหัวใจ</li>
         <li>การหลีกเลี่ยงการบริโภคอาหารที่มีสารอาหารไม่ดี:ลดการบริโภคอาหารที่มีโคเลสเตอรอลสูง, น้ำตาล, และเกลือ</li>
      </ul>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">การปฏิบัติตนตามแนวทางดังกล่าวจะช่วยลดโอกาสที่จะเป็นโรคหัวใจวายและส่งเสริมสุขภาพหัวใจที่แข็งแรง. อย่าลืมปรึกษาแพทย์หากคุณมีปัญหาสุขภาพหรือต้องการคำแนะนำเพิ่มเติมเกี่ยวกับการรักษาและป้องกันโรคหัวใจวาย</h6></left>
      </div>
      """
      st.markdown(html_9, unsafe_allow_html=True)
      st.markdown("")