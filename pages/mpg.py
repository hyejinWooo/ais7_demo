import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚗",
    layout="wide",
)

st.markdown("# 자동차 연비 🚗")
st.sidebar.markdown("# 자동차 연비 🚗")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"

@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

data_load_state = st.text('Loading data...')
data = load_data(url)
data_load_state.text("Done! (using st.cache)")

# 큰 순서대로 나타내기 위해
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(data.model_year.min(),data.model_year.max())))
   )

# Sidebar - origin
sorted_unique_origin = sorted(data.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)


if selected_year > 0 :
   data = data[data.model_year == selected_year]

# 국가 선택
if len(selected_origin) > 0:
   data = data[data.origin.isin(selected_origin)]
   
st.dataframe(data)

st.line_chart(data["mpg"])

st.bar_chart(data["mpg"])

# sns.countplot(data=data, x="origin") -> 이렇게 하면 출력 안 됨 서류 참고하기

# plt.subplots()를 하면 두가지가 반환는데 각 변수를 fig, ax로 지정
fig, ax = plt.subplots(figsize=(10,3))
sns.countplot(data=data, x="origin").set_title("지역별 자동차 연비 데이터 수")
st.pyplot(fig)

pxh = px.histogram(data, x="origin", title = "지역별 자동차 연비 데이터 수")
st.plotly_chart(pxh)

cp = sns.catplot(data=data, x='horsepower', y='weight', hue='origin', ci=None)
st.pyplot(cp)