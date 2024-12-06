import streamlit as st

# Streamlit App
st.title("🎓 RAI HANAN Calculator")

st.write("""
### Calculate your GPA easily by entering your grades and credit hours for each course.
""")

# Input section
num_courses = st.number_input("Enter the number of courses:", min_value=1, step=1)

grades = []
credit_hours = []

st.write("### Enter your grades and credit hours for each course:")
for i in range(num_courses):
    st.write(f"#### Course {i+1}")
    grade = st.selectbox(f"Select grade for Course {i+1}:", 
                         options=["A", "B", "C", "D", "F"], 
                         index=0, key=f"grade_{i}")
    credit = st.number_input(f"Enter credit hours for Course {i+1}:", 
                             min_value=1, max_value=5, step=1, key=f"credit_{i}")
    
    grades.append(grade)
    credit_hours.append(credit)

# Grade to GPA mapping
grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

# Calculate GPA
if st.button("Calculate GPA"):
    total_points = 0
    total_credits = 0
    for i in range(num_courses):
        total_points += grade_points[grades[i]] * credit_hours[i]
        total_credits += credit_hours[i]
    
    if total_credits > 0:
        gpa = total_points / total_credits
        st.success(f"Your GPA is: **{gpa:.2f}**")
    else:
        st.error("Total credits cannot be zero!")

st.write("### Instructions")
st.write("""
1. Enter the number of courses.
2. Select the grade and credit hours for each course.
3. Click **Calculate GPA** to see your result.
""")
