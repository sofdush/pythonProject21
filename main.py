import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
#  ставим картинку
st.image('titanic.jpg')
# читаем таблицу
titanic_data = pd.read_csv('data.csv')
# названия для списка и как они в таблице
cities = {'Шербур (C)': 'C', 'Квинстаун (Q)': 'Q', 'Саутгемптон (S)': 'S'}
# делаем описание страницы
st.header('Данные пассажиров с титаника')
st.write('Для просмотра средней стоимости билета пассажира выберите порт посадки (Шербур, Квинстаун, Саутгемптон)')
# выпадающий список для выбора города
option = st.selectbox(label='Выберите порт посадки', options=list(cities.keys()))
# из таблицы титаника выбираем по выбранному порту посадки
filtered_df = titanic_data[titanic_data['Embarked'] == cities[option]]
# фильтруем данные по статусу выживания и средней стоимости билета
# c использованием соответствующих функций groupby и mean из библиотеки pandas
# https://sky.pro/media/rabota-s-gruppovymi-statistikami-v-pandas-groupby/
avg_price = filtered_df.groupby('Survived', as_index=False)['Fare'].mean()
# рисуем табличку
st.table({'Статус': ['Погиб', 'Выжил'], 'Средняя цена': avg_price['Fare']})
# создаем диаграмму
fig = plt.figure(figsize=(10, 5))
plt.bar(['Погиб', 'Выжил'], avg_price['Fare'], color=['red', 'green'])
plt.xlabel('Статус')
plt.ylabel('Средняя цена')
plt.suptitle('Средняя стоимость поездки для выживших и погибших пассажиров')
st.pyplot(fig)
