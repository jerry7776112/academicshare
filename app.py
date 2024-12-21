import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

conference = pd.read_csv("data\computerscience1.csv", encoding='utf-8-sig')
journal = pd.read_csv("data\computerscience2.csv", encoding='utf-8-sig')

df = pd.concat([conference, journal], axis=0)
# df = pd.DataFrame()

st.set_page_config( 
    page_title="Academic Freedom", # 頁籤名稱 
    page_icon="👁️", # 頁籤圖標，可以使用 emoji 或 URL 
    # layout="centered", # 頁面佈局 
    # initial_sidebar_state="auto" # 側邊欄狀態 
    )

config = {
    # "_index": st.column_config.TextColumn("順序"),
    "會議簡稱": st.column_config.TextColumn("會議簡稱"),
    "會議全名": st.column_config.TextColumn("會議全名"),
    "分類": st.column_config.TextColumn("分類"),
    "類型": st.column_config.TextColumn("類型"),
    "專業領域": st.column_config.TextColumn("專業領域")
}

# Streamlit 應用 
st.title('Academic Freedom')
st.header("資訊工程系列")
st.subheader('條件篩選')
# st.sidebar.success("Select a demo above.")
# 篩選選項
types = ['顯示全部'] + df['類型'].unique().tolist() 
fields = ['顯示全部'] + df['專業領域'].unique().tolist()
categories = ['顯示全部'] + df['分類'].unique().tolist() 

selected_type = st.selectbox('選擇類型', types) 
selected_field = st.selectbox('選擇專業領域', fields)
selected_category = st.selectbox('選擇分類', categories) 

# 篩選數據
filtered_df = df[ 
    ((df['類型'] == selected_type) | (selected_type == '顯示全部')) & 
    ((df['專業領域'] == selected_field) | (selected_field == '顯示全部')) &
    ((df['分類'] == selected_category) | (selected_category == '顯示全部'))
    ]

# 顯示篩選結果 
st.write('篩選結果：') 
# st.dataframe(filtered_df)
# st.dataframe(df.style.hide(axis="index"), column_config=config)
# st.dataframe(df.style.highlight_max(axis=0))
st.markdown(filtered_df.style.hide(axis="index").to_html(), unsafe_allow_html=True)

# AdSense 程式碼 
adsense_code = """ 
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5870212936948418"
     crossorigin="anonymous"></script>
<!-- AcademicFreedom -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-5870212936948418"
     data-ad-slot="6889789127"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script> 
""" 
# # 在 Streamlit 應用中嵌入 AdSense 程式碼 
components.html(adsense_code)