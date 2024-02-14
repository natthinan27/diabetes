import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
import matplotlib.gridspec as gridspec


html_1 = """
<div style="background-color:#87A5E0;margin-top:40px;padding:5px;border-radius:5px;border-bottom: 3px solid #31333F;border-top: 3px solid #31333F;">
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

html_3 = """
<div style="background-color:#87A5E0;border-bottom: 3px solid #31333F;border-top: 3px solid #31333F;">
<center><h3>Example data table</h3></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")
st.write(df.head(10))

html_4 = """
<div style="background-color:#87A5E0;border-bottom: 3px solid #31333F;border-top: 3px solid #31333F;">
<center><h3>Count plot for various categorical features</h3></center>
</div>
"""
st.markdown(html_4, unsafe_allow_html=True)
st.markdown("")

fig = plt.figure(figsize=(18, 15))
gs = fig.add_gridspec(3, 3)
gs.update(wspace=0.5, hspace=0.25)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[0, 1])
ax2 = fig.add_subplot(gs[0, 2])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax5 = fig.add_subplot(gs[1, 2])
ax6 = fig.add_subplot(gs[2, 0])
ax7 = fig.add_subplot(gs[2, 1])
ax8 = fig.add_subplot(gs[2, 2])

background_color = "#ffe6e6"
color_palette = ["#800000", "#8000ff", "#6aac90", "#5833ff", "#da8829"]
fig.patch.set_facecolor(background_color)
ax0.set_facecolor(background_color)
ax1.set_facecolor(background_color)
ax2.set_facecolor(background_color)
ax3.set_facecolor(background_color)
ax4.set_facecolor(background_color)
ax5.set_facecolor(background_color)
ax6.set_facecolor(background_color)
ax7.set_facecolor(background_color)
ax8.set_facecolor(background_color)

# Title of the plot
ax0.spines["bottom"].set_visible(False)
ax0.spines["left"].set_visible(False)
ax0.spines["top"].set_visible(False)
ax0.spines["right"].set_visible(False)
ax0.tick_params(left=False, bottom=False)
ax0.set_xticklabels([])
ax0.set_yticklabels([])
ax0.text(0.5, 0.5,
         'Count plot for various\n categorical features\n_________________',
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=18, fontweight='bold',
         fontfamily='serif',
         color="#000000")

# Function to create count plot using bar
def create_count_plot(ax, data, x, palette):
    ax.bar(data[x].value_counts().index, data[x].value_counts().values, color=palette)
    ax.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
    ax.set_xlabel("")
    ax.set_ylabel("")

# Sex count
ax1.text(0.3, 165, 'Sex', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax1, df, 'sex', color_palette)
ax1.set_xticks([0, 1])
ax1.set_xticklabels(["Female(0)", "Male(1)"])

# Exng count
ax2.text(0.3, 160, 'Exng', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax2, df, 'exng', color_palette)
ax2.set_xticks([0, 1])
ax2.set_xticklabels(["No(0)","Yes(1)"])

# Caa count
ax3.text(1.5, 120, 'Caa', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax3, df, 'caa', color_palette)
ax3.set_xticks([0, 1,2,3,4])


# Cp count
ax4.text(1.5, 120, 'Cp', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax4, df, 'cp', color_palette)
ax4.set_xticks([0,1,2,3])
ax4.set_xticklabels(["Typical angina(1)","Atypical angina(2)","nopain(3)","asymptomatic(4)"], rotation=15)

# Fbs count
ax5.text(0.5, 200, 'Fbs', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax5, df, 'fbs', color_palette)
ax5.set_xticks([0, 1])
ax5.set_xticklabels(["False(0)","True(1)"])

# Restecg count
ax6.text(0.75, 120, 'Restecg', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax6, df, 'restecg', color_palette)
ax6.set_xticks([0, 1,2])
ax6.set_xticklabels(["normal(0)","ST-T abnormality (1)","LV hypertrophy(2)"], rotation=15)

# Slp count
ax7.text(0.85, 120, 'Slp', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax7, df, 'slp', color_palette)
ax7.set_xticks([0, 1,2])

# Thall count
ax8.text(1.2, 120, 'Thall', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax8, df, 'thall', color_palette)
ax8.set_xticks([0, 1, 2, 3])

# Remove spines
for s in ["top", "right", "left"]:
    ax1.spines[s].set_visible(False)
    ax2.spines[s].set_visible(False)
    ax3.spines[s].set_visible(False)
    ax4.spines[s].set_visible(False)
    ax5.spines[s].set_visible(False)
    ax6.spines[s].set_visible(False)
    ax7.spines[s].set_visible(False)
    ax8.spines[s].set_visible(False)


st.pyplot(fig)

html_5 = """
<div style="background-color:#87A5E0;border-bottom: 3px solid #31333F;border-top: 3px solid #31333F;">
<center><h3>Count of the target</h3></center>
</div>
"""
st.markdown(html_5, unsafe_allow_html=True)
st.markdown("")



fig = plt.figure(figsize=(18, 7))
gs = fig.add_gridspec(1, 2)
gs.update(wspace=0.3, hspace=0.15)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[0, 1])

background_color = "#ffe6e6"
color_palette = ["#800000", "#8000ff", "#6aac90", "#5833ff", "#da8829"]
fig.patch.set_facecolor(background_color)
ax0.set_facecolor(background_color)
ax1.set_facecolor(background_color)

# Title of the plot
ax0.text(0.5, 0.5, "Count of the target\n___________",
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=18,
         fontweight='bold',
         fontfamily='serif',
         color='#000000')

ax0.set_xticklabels([])
ax0.set_yticklabels([])
ax0.tick_params(left=False, bottom=False)

# Target Count
ax1.text(0.35, 130, "Output", fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
ax1.bar(df['output'].value_counts().index, df['output'].value_counts().values, color=color_palette)
ax1.set_xlabel("")
ax1.set_ylabel("")
ax1.set_xticks([0, 1])
ax1.set_xticklabels(["Low chances of attack(0)", "High chances of attack(1)"])

# Remove spines
for s in ["top", "left", "right"]:
    ax0.spines[s].set_visible(False)
    ax1.spines[s].set_visible(False)
st.pyplot(fig)


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
s1 = st.number_input("# Age : อายุของผู้ป่วย")
s2 = st.selectbox("# Sex : เพศของผู้ป่วย (0 : หญิง | 1 : ชาย)", [0, 1])
s3 = st.selectbox("# Cp : อาการเจ็บหน้าอก\n(0 : โรคหลอดเลือดหัวใจตีบทั่วไป | 1 : โรคหลอดเลือดหัวใจตีบผิดปรกติ | 2 : อาการปวดที่ไม่ใช่โรคหลอดเลือดหัวใจตีบ | 3 : ไม่มีอาการ)", [0, 1, 2, 3])
s4 = st.number_input("# Trtbps : ความดันโลหิตขณะพัก (มม. ปรอท)")
s5 = st.number_input("# Chol : cholestoral ใน mg/dl ดึงผ่านเซ็นเซอร์ BMI")
s6 = st.selectbox("# Fbs : น้ําตาลในเลือดขณะอดอาหาร > 120 มก./ดล. (1 = จริง 0 = เท็จ)", [0, 1])
s7 = st.selectbox("# Restecg : พักผลการตรวจคลื่นไฟฟ้าหัวใจ ( 0 : ปกติ | 1 : มีความผิดปกติของคลื่น ST-T | 2 : แสดงกระเป๋าหน้าท้องยั่วยวนซ้ายที่เป็นไปได้หรือแน่นอนตามเกณฑ์ของเอสเตส)", [0, 1, 2])
s8 = st.number_input("# Thalachh : อัตราการเต้นของหัวใจสูงสุดทําได้")
s9 = st.selectbox("# Exng : การออกกําลังกายทําให้เกิดโรคหลอดเลือดหัวใจตีบ (1 = ใช่ 0 = ไม่ใช่)", [0, 1])
s10 = st.number_input("# Oldpeak : จุดสูงสุดก่อนหน้า")
s11 = st.selectbox("# Slp : Slope", [0, 1, 2])
s12 = st.selectbox("# Caa : Number of major vessels (0-3)", [0, 1, 2, 3])
s13 = st.selectbox("# Thall : Thal rate", [0, 1, 2, 3])

# Adjusting font size and making it bold
st.markdown("<style>h1{font-size: 18px !important;}</style>", unsafe_allow_html=True)
st.markdown("<style>label{font-size: 16px !important; font-weight: bold;}</style>", unsafe_allow_html=True)

if st.button("ทำนายผล"):

   X=df.drop(["output"],axis=1)
   y=df["output"]

   nb_model = GaussianNB()
   nb_model.fit(X, y)


   x_input = np.array([[s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13]])

   out = nb_model.predict(x_input)

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