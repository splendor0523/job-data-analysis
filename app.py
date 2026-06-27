from pathlib import Path
import streamlit as st
import pandas as pd
from scripts.analyze_jobs import (load_data,validate_data,create_analysis_results)


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "jobs.csv"

st.title("Job Data Analysis Dashboard")
st.write(
    "This is a simple Streamlit dashboard for exploring job posting data"
)

uploaded_file = st.file_uploader(
    "Upload a jobs CSV file",
    type=["csv"]
)

try:
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = load_data(DATA_PATH)

    df = validate_data(df)

    
except FileExistsError as e:
    st.error("Default data file was not found.")
    st.code(str(e))
    st.stop()

except ValueError as e:
    st.error("The CSV file format is invalid.")
    st.code(str(e))
    st.stop()

except Exception as e:
    st.error("Unexpected error while loading data.")
    st.code(str(e))
    st.stop()

if uploaded_file is not None:
    st.success("Uploaded CSV file loaded successfully.")
else:
    st.info("Using default sample data: data/jobs.csv")

st.sidebar.header("Filters")
filtered_df = df.copy()
cities = sorted(df["city"].dropna().unique())

selected_cities = st.sidebar.multiselect(
    "Select cities",
    options=cities,
    default=cities
)
if selected_cities:
    filtered_df = filtered_df[filtered_df["city"].isin(selected_cities)]

skill_keyword = st.sidebar.text_input(
    "Search skill keyword",
    value="" 
)

if skill_keyword:
    filtered_df = filtered_df[
        filtered_df["skills"].str.contains(skill_keyword,case=False,na=False)
        ]

min_salary = int(df["salary"].min())
max_salary = int(df["salary"].max())

if min_salary < max_salary:
    salary_range = st.sidebar.slider(
        "Salary range",
        min_value = min_salary,
        max_value = max_salary,
        value= (min_salary,max_salary)
    )

    filtered_df = filtered_df[
        filtered_df["salary"].between(salary_range[0],salary_range[1])
        ]

if filtered_df.empty:
    st.warning("No jobs match the current filters.")
    st.stop()

results = create_analysis_results(filtered_df)

st.subheader("Key Metrics")
col1,col2,col3,col4 = st.columns(4)
col1.metric("Total Jobs", results["total_jobs"])
col2.metric("Average Salary", f"{results['avg_salary']:.2f}")
col3.metric("Python Jobs", results["python_job_count"])
col4.metric("Data Analysis Jobs", results["data_analysis_job_count"])

st.subheader("City Counts")
st.dataframe(results["city_counts"])

st.subheader("Skill Counts")
st.dataframe(results["skill_counts"])

st.subheader("Top Skills Chart")
skill_chart_data = (
    results["skill_counts"]
    .head(10)
    .set_index("skill")
)
st.bar_chart(skill_chart_data)

st.subheader("Average Salary by City")
city_salary_chart_data = (
    results["city_salary_sorted"]
    .set_index("city")
)
st.bar_chart(city_salary_chart_data)

st.subheader("Top High Salary Jobs")
st.dataframe(results["high_salary_jobs"].head(10))

st.subheader("Original Job Data")
st.dataframe(filtered_df)