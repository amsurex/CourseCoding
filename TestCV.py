import streamlit as st
import numpy as np 

st.title('Реши следующее задание.')

with st.form('Ответьте на все вопросы, чтобы успешно завершить задание.'):

# Вопросы 
    st.markdown('**Вопрос 1:** С помощью чего получают изображение страниц текста?')
    q1_right_1 = st.checkbox('Сканер.', value=False, key='1') 
    q1_wrong_2 = st.checkbox('Принтер.', value=False, key='2')
    q1_right_3 = st.checkbox('Компьютер.', value=False, key='3') 
    q1_wrong_4 = st.checkbox('Интернет.', value=False, key='4')

    st.markdown('**Вопрос 2:** Если исходный документ имеет плохое типографское качество печати, то каким методом будет решаться задача распознавания?')
    q2_right_1 = st.checkbox('Сравнения с растровым шаблоном.', value=False, key='7') 
    q2_wrong_2 = st.checkbox('Сопоставления.', value=False, key='8')
    q2_wrong_3 = st.checkbox('Интерполяция.', value=False, key='9') 
    q2_wrong_4 = st.checkbox('Нет такого метода.', value=False, key='10')

    st.markdown('**Вопрос 3:** Любой ли символ можно описать через набор параметров?')
    q3_wrong_1 = st.checkbox('Только символ хорошего качества.', value=False, key='11') 
    q3_wrong_2 = st.checkbox('Только символ хорошо изображенный.', value=False, key='12') 
    q3_wrong_3 = st.checkbox('Не знаю.', value=False, key='13')
    q3_right_4 = st.checkbox('Любой.', value=False, key='14')

    st.markdown('**Вопрос 4:** Рукопечатные тексты распознаются с помощью ... ?')
    q4_wrong_1 = st.checkbox('Систем оптического распознавания форм.',value=False, key='15')
    q4_wrong_2 = st.checkbox('Сопоставления.', value=False, key='16')
    q4_wrong_3 = st.checkbox('Нет правильного ответа.', value=False, key='17') 
    q4_right_4 = st.checkbox('Систем оптического распознавания форм и сопоставления одновременно.', value=False, key='18')
 
    st.markdown('**Вопрос 5:** В окне системы оптического распознования текста появляется ... ?')
    q5_right_1 = st.checkbox('Растровый рисунок.', value=False, key='20') 
    q5_wrong_2 = st.checkbox('Отсканированное изображение текстовой страницы.', value=False, key='21')
    q5_wrong_3 = st.checkbox('Векторный рисунок.', value=False, key='22') 
    q5_wrong_4 = st.checkbox('Текстовый документ.', value=False, key='23')

# Проверка правильных и неправильных ответов 
    right_answers = (q1_right_1 and q1_right_3 and q2_right_1 and q3_right_4 and q4_right_4 and q5_right_1)
    wrong_answers = (q1_wrong_2 or q1_wrong_4 or q2_wrong_2 or q2_wrong_3 or 
                     q2_wrong_4 or q3_wrong_1 or q3_wrong_2 or q3_wrong_3 or 
                     q4_wrong_1 or q4_wrong_2 or q4_wrong_3 or q5_wrong_2 or 
                     q5_wrong_3 or q5_wrong_4)

# Вывод результата
    if right_answers and not wrong_answers:
        st.success('Верно! Ты большой молодец!') 
    if wrong_answers and not right_answers: 
        st.error('Не получилось! Попробуй еще раз :(')

# Кнопка, чтобы отправить форму
    st.form_submit_button('Отправить')