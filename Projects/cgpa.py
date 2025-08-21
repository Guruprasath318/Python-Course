import streamlit as st

st.title("CGPA Calculator")

st.write("Enter your grades below:")

grades = []
for i in range(1, 6):
    grade = st.number_input(f"Grade {i}", 0.0, 100.0, 0.0)
    grades.append(grade)

if st.button("Calculate CGPA"):
    cgpa = sum(grades) / len(grades)
    st.success(f"Your CGPA is: {cgpa:.2f}")



# To run this code, save it as cgpa.py and run the following command in your terminal:
#streamlit run cgpa.py

