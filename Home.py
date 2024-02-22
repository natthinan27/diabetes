import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
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
<div style="background-color:#E799A3;border-bottom: 3px solid #31333F;border-top: 3px solid #31333F;">
<center><h3>Example data table</h3></center>
</div>
"""
st.markdown(html_6, unsafe_allow_html=True)
st.markdown("")
st.write(df.head(10))

html_7 = """
<div style="background-color:E799A3;border-bottom: 3px solid #31333F;border-top: 3px solid #31333F;margin-top:20px;">
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
#s9 = st.selectbox("# Outcome : ผลลัพธ์สุดท้าย  (1 = ใช่ 0 = ไม่ใช่)", [0, 1])

# Adjusting font size and making it bold
st.markdown("<style>h1{font-size: 18px !important;}</style>", unsafe_allow_html=True)
st.markdown("<style>label{font-size: 16px !important; font-weight: bold;}</style>", unsafe_allow_html=True)
st.markdown('<div style="text-align:center"><br></div>', unsafe_allow_html=True)
if st.button("ทำนายผล"):
   
   X=df.drop(["Outcome"],axis=1)
   y=df["Outcome"]

   rf_model = RandomForestClassifier()
   rf_model.fit(X, y)



   x_input = np.array([[s1, s2, s3, s4, s5, s6, s7, s8]])

   out = rf_model.predict(x_input)

   if out[0]== 0 :

          
      html_11 = """
      <div style="background-color:#EEEEEE;padding:5px;border: 3px solid #;">
      <center><h2 border: 2px solid #000000;>Prediction Result</h2></center>
      </div>
      """
      st.markdown(html_11, unsafe_allow_html=True)
      st.markdown("")
          
      html_8 = """
      <div style="background-color:#EEEEEE;padding:20px;border: 3px solid #31333F;">
      <center><h3>ความเสี่ยงโรคเบาหวานต่ำ</h3></center>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">โรคเบาหวาน (Diabetes) คือโรคที่เกิดจากความผิดปกติของการทำงานของฮอร์โมนที่ชื่อว่า อินสุลิน (Insulin) ซึ่งโดยปกติแล้วร่างกายของคนเราจำเป็นต้องมีอินสุลิน เพื่อนำน้ำตาลในกระแสเลือดไปเลี้ยงอวัยวะต่าง ๆ ของร่างกาย โดยเฉพาะสมองและกล้ามเนื้อ ในภาวะที่อินสุลินมีความผิดปกติ ไม่ว่าจะเป็นการลดลงของปริมาณอินสุลินในร่างกาย หรือการที่อวัยวะต่าง ๆ ของร่างกายตอบสนองต่ออินสุลินลดลง (หรือที่เรียกว่า ภาวะดื้ออินสุลิน) จะทำให้ร่างกายไม่สามารถนำน้ำตาลที่อยู่ในกระแสเลือดไปใช้ได้อย่างเต็มประสิทธิภาพ ทำให้มีปริมาณน้ำตาลคงเหลือในกระแสเลือดมากกว่าปกติ</h6></left>

      </div>
      """
      st.markdown(html_8, unsafe_allow_html=True)
      st.markdown("")

      html_9 = """
      <div style="background-color:#EEEEEE;padding:20px;border: 3px solid #31333F;">
      <center><h3 style="border-bottom: 3px solid #31333F;">คำแนะนำ</h3></center>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">วิธีการป้องกันโรคเบาหวาน</h6></left>
      <ul>
         <li>ควบคุมน้ำหนัก: การรักษาน้ำหนักที่เหมาะสมหรือลดน้ำหนักหากมีน้ำหนักเกินมาจะช่วยลดความเสี่ยงในการเป็นโรคเบาหวาน</li>
         <li>ออกกำลังกาย: การออกกำลังกายเป็นประจำช่วยลดระดับน้ำตาลในเลือดและเพิ่มความได้รับอินซูลิน แนะนำให้ออกกำลังกายอย่างสม่ำเสมออย่างน้อย 150 นาทีต่อสัปดาห์</li>
         <li>ควบคุมอาหาร: ลดการบริโภคอาหารที่มีน้ำตาลและไขมันสูง เพิ่มการบริโภคผักผลไม้ และเลือกทานอาหารที่มีระดับโภชนาการสูง</li>
         <li>ลดการบริโภคเครื่องดื่มที่มีน้ำตาล: ลดหรือหลีกเลี่ยงการดื่มเครื่องดื่มที่มีน้ำตาลเพิ่ม เช่น น้ำอัดลมและเครื่องดื่มชนิดอื่นๆ</li>
         <li>หมั่นตรวจสุขภาพ: ตรวจระดับน้ำตาลในเลือดอย่างสม่ำเสมอ และรับการตรวจสุขภาพประจำเพื่อตรวจจับภาวะที่เสี่ยงต่อโรคเบาหวานต่างๆ</li>
         <li>หลีกเลี่ยงสุราและบุหรี่: การดื่มสุราอย่างมีสมาธิ และการหลีกเลี่ยงการสูบบุหรี่ช่วยลดความเสี่ยงต่อการเป็นโรคเบาหวาน</li>
         <li>รักษาความเครียด: การรักษาสุขภาพจิตและลดความเครียด มีผลต่อการควบคุมระดับน้ำตาลในเลือดได้</li>
      </ul>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">การป้องกันโรคเบาหวานมักจะเน้นไปที่การรักษาพฤติกรรมที่เปลี่ยนแปลงได้ และการสร้างนิสัยการดูแลสุขภาพที่ดี โดยการปฏิบัติตามแนวทางดังกล่าวอาจช่วยลดความเสี่ยงต่อโรคเบาหวานอย่างมีประสิทธิภาพ</h6></left>
      </div>
      """
      st.markdown(html_9, unsafe_allow_html=True)
      st.markdown("")
      

   elif out[0]==1: 
          
      html_10 = """
      <div style="background-color:#EEEEEE;padding:20px;border: 3px solid #31333F;">
      <center><h3 style="border-bottom: 3px solid #31333F;">มีโอกาสเป็นเบาหวานสูง</h3></center>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">โรคเบาหวาน (Diabetes) คือโรคที่เกิดจากความผิดปกติของการทำงานของฮอร์โมนที่ชื่อว่า อินสุลิน (Insulin) ซึ่งโดยปกติแล้วร่างกายของคนเราจำเป็นต้องมีอินสุลิน เพื่อนำน้ำตาลในกระแสเลือดไปเลี้ยงอวัยวะต่าง ๆ ของร่างกาย โดยเฉพาะสมองและกล้ามเนื้อ ในภาวะที่อินสุลินมีความผิดปกติ ไม่ว่าจะเป็นการลดลงของปริมาณอินสุลินในร่างกาย หรือการที่อวัยวะต่าง ๆ ของร่างกายตอบสนองต่ออินสุลินลดลง (หรือที่เรียกว่า ภาวะดื้ออินสุลิน) จะทำให้ร่างกายไม่สามารถนำน้ำตาลที่อยู่ในกระแสเลือดไปใช้ได้อย่างเต็มประสิทธิภาพ ทำให้มีปริมาณน้ำตาลคงเหลือในกระแสเลือดมากกว่าปกติ</h6></left>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">วิธีการป้องกันโรคเบาหวาน</h6></left>
      <ul>
         <li>ควบคุมน้ำหนัก: การรักษาน้ำหนักที่เหมาะสมหรือลดน้ำหนักหากมีน้ำหนักเกินมาจะช่วยลดความเสี่ยงในการเป็นโรคเบาหวาน</li>
         <li>ออกกำลังกาย: การออกกำลังกายเป็นประจำช่วยลดระดับน้ำตาลในเลือดและเพิ่มความได้รับอินซูลิน แนะนำให้ออกกำลังกายอย่างสม่ำเสมออย่างน้อย 150 นาทีต่อสัปดาห์</li>
         <li>ควบคุมอาหาร: ลดการบริโภคอาหารที่มีน้ำตาลและไขมันสูง เพิ่มการบริโภคผักผลไม้ และเลือกทานอาหารที่มีระดับโภชนาการสูง</li>
         <li>ลดการบริโภคเครื่องดื่มที่มีน้ำตาล: ลดหรือหลีกเลี่ยงการดื่มเครื่องดื่มที่มีน้ำตาลเพิ่ม เช่น น้ำอัดลมและเครื่องดื่มชนิดอื่นๆ</li>
         <li>หมั่นตรวจสุขภาพ: ตรวจระดับน้ำตาลในเลือดอย่างสม่ำเสมอ และรับการตรวจสุขภาพประจำเพื่อตรวจจับภาวะที่เสี่ยงต่อโรคเบาหวานต่างๆ</li>
         <li>หลีกเลี่ยงสุราและบุหรี่: การดื่มสุราอย่างมีสมาธิ และการหลีกเลี่ยงการสูบบุหรี่ช่วยลดความเสี่ยงต่อการเป็นโรคเบาหวาน</li>
         <li>รักษาความเครียด: การรักษาสุขภาพจิตและลดความเครียด มีผลต่อการควบคุมระดับน้ำตาลในเลือดได้</li>
      </ul>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">การป้องกันโรคเบาหวานมักจะเน้นไปที่การรักษาพฤติกรรมที่เปลี่ยนแปลงได้ และการสร้างนิสัยการดูแลสุขภาพที่ดี โดยการปฏิบัติตามแนวทางดังกล่าวอาจช่วยลดความเสี่ยงต่อโรคเบาหวานอย่างมีประสิทธิภาพ</h6></left>
      </div>
      """
      st.markdown(html_9, unsafe_allow_html=True)
      st.markdown("")