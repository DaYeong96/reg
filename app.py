
#streamlit 라이브러리를 불러오기
import streamlit as st
#AI모델을 불러오기 위한 joblib 불러오기
import joblib
import pandas as pd
import pickle 

# st를 이용하여 타이틀과 입력 방법을 명시한다.

def user_input_features():
    dist = st.sidebar.number_input("거리: ")
    office =st.sidebar.number_input("오피스비중: ")
    home = st.sidebar.number_input("홈비중: ")
    co2 = st.sidebar.number_input("일산화탄소양: ")
    room =st.sidebar.number_input("방수: ")
    age = st.sidebar.number_input("연수: ")
    pop = st.sidebar.number_input("유동인구수: ")
    road = st.sidebar.slider("고속도로: ",0, 25)
    mange = st.sidebar.slider("관리비: ", 100, 800)
    kid = st.sidebar.number_input("아이들비중: ")
    station =st.sidebar.slider("역근처 여부: ", 0,1)

    data = {'dist' : [dist],
            'office' : [office],
            'home' : [home],
            'co2' : [co2],
            'room' : [room],
            'age' : [age],
            'pop' : [pop],
            'road' : [road],
            'mange' : [mange],
            'kid' : [kid],
            'station' : [station]
            }
    data_df = pd.DataFrame(data, index=[0])
    return data_df

# new_x= {'dist':[0.03], 'office':[10], 'home':[2.22], 'station':[1], 'co2':[0.66], 'room' : [8.33],'age':[23.1], 'pop':[4.11], 'road':[12], 'mange':[323], 'kid':[12.23] }


st.title('렌탈료 예측 서비스')
st.markdown('* 우측에 데이터를 입력해주세요')


ohe_station = joblib.load('ohe_station.joblib')
scaler_call = joblib.load('scaler.save')
#model_call = joblib.load("model.pkl")
model_call = pickle.load(open('model.pkl', 'rb')


new_x_df = user_input_features()
st.dataframe(new_x_df)

st.dataframe(new_x_df[['station']])
st.write(new_x_df['station'].dtype)

data_cat2 = ohe_station.transform(new_x_df[['station']])
data_concat = pd.concat([new_x_df.drop(columns=['station']),pd.DataFrame(data_cat2, columns=['station_' + str(col) for col in ohe_station.categories_[0]])], axis=1)





data_con_scale = scaler_call.transform(data_concat)
result = model_call.predict(data_con_scale) 

#예측결과를 화면에 뿌려준다. 
st.subheader('결과는 다음과 같습니다.')
st.write('예상되는 렌탈료:', result[0])
