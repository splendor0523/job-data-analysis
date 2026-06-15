import pandas as pd
import argparse
from pathlib import Path
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR/"data"
OUTPUT_DIR = BASE_DIR/"output"
OUTPUT_DIR.mkdir(exist_ok=True)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze job posting data with pandas"
    )

    parser.add_argument(
        "--input",
        default=str(DATA_DIR / "jobs.csv"),
        help="Path to the input jobs CSV file"
    )
    parser.add_argument(
        "--output",
        default=str(OUTPUT_DIR),
        help="Directory to save output files"
    )
    return parser.parse_args()

args = parse_args()

input_path = Path(args.input)
output_dir = Path(args.output)

if not input_path.is_absolute():
    input_path = BASE_DIR / input_path
if not output_dir.is_absolute():
    output_dir = BASE_DIR /output_dir

output_dir.mkdir(exist_ok=True,parents=True)

if not input_path.exists():
    raise FileExistsError(
        f"Input file not found : {input_path}\n"
        f"please make sure job.csv exists in the data folder"
    )

df = pd.read_csv(input_path)

def save_bar_chart(data,x_col,y_col,title,xlabel,ylabel,output_path,top_n=None):
    plot_data = data.copy()

    if top_n is None:
        plot_data = plot_data.head(top_n)

    plt.figure(figsize=(10,6))
    plt.bar(plot_data[x_col], plot_data[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


required_columns = {"title","city","salary","skills"}
actual_columns = set(df.columns)
missing_columns = required_columns - actual_columns
if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}\n"
        f"Required columns are: {required_columns}"
    )

df["salary"] = pd.to_numeric(df["salary"],errors="coerce")
if df["salary"].isna().any():
    raise ValueError(
         "The salary column contains invalid values. "
        "Please make sure all salary values are numbers."
    )

print("Original data:")
print(df)

print("\nBasic info:")
df.info()

print("\nFirst 5 rows")
print(df.head())

# ============================================================================

data_analyze_jobs = df[df["title"].str.contains("数据分析",na=False)]
data_analyze_skill_counts = (
    data_analyze_jobs["skills"]
    .str.split(";")
    .explode()
    .str.strip()
    .value_counts()
    .rename_axis("skill")
    .reset_index(name="count")
)
print("\nData analysis jobs:")
print(data_analyze_jobs)

print("\nData analysis job skill counts:")
print(data_analyze_skill_counts)

data_analyze_skill_counts.to_csv(
    output_dir/"data_analysis_skill_counts.csv",
    index=False
)

#==================================================================

city_counts = df["city"].value_counts()
print("\nCity counts:")
print(city_counts)

title_counts = df["title"].value_counts()
print("\nTitle counts:")
print(title_counts)

python_jobs = df[df["skills"].str.contains("Python",na=False)]
print("\nPython jobs:")
print(python_jobs)

# ============================================================================

skill_counts_df = (df["skills"]
               .str.split(";")
               .explode()
               .str.strip()
               .value_counts()
               .rename_axis("skill")
               .reset_index(name = "count")
               )
print("\nSkills counts:")
print(skill_counts_df)

# ===========================================================================

city_salary = (
    df.groupby("city")["salary"]
    .mean()
    .round(2)
    .rename_axis("city")
    .reset_index(name="avg_salary")
)
print("\nAverage salary by city:")
print(city_salary) 

city_salary_sorted =city_salary.sort_values(by="avg_salary",ascending=False)
print("\nAverage salary by city sorted:")
print(city_salary_sorted)
city_salary_sorted.to_csv(output_dir/"city_avg_salary_sorted.csv",index=False)

city_salary.to_csv(output_dir/"city_avg_salary.csv", index=False)

# =========================================================

high_salary_job = df.sort_values(by="salary",ascending=False)
high_salary_jobs = df.sort_values(by="salary", ascending=False)

print("\nHigh salary jobs:")
print(high_salary_jobs)

high_salary_jobs.to_csv(output_dir/"high_salary_jobs.csv", index=False)

save_bar_chart(
    data=skill_counts_df,
    x_col="skill",
    y_col="count",
    title="Top Skills in Job Posts",
    xlabel="Skill",
    ylabel="Count",
    output_path=output_dir / "skill_counts.png",
    top_n=10
)

save_bar_chart(
    data=city_salary_sorted,
    x_col="city",
    y_col="avg_salary",
    title="Average Salary by City",
    xlabel="City",
    ylabel="Average Salary",
    output_path=output_dir / "city_avg_salary.png"
)

save_bar_chart(
    data=high_salary_jobs.head(10),
    x_col="title",
    y_col="salary",
    title="Top Salary Jobs",
    xlabel="Job Title",
    ylabel="Salary",
    output_path=output_dir / "high_salary_jobs.png"
)

# ===================================================================
data_analyze_jobs.to_csv(output_dir/"data_analysis_jobs.csv", index=False)
city_counts.to_csv(output_dir/"city_counts.csv", header=["count"])
title_counts.to_csv(output_dir/"title_counts.csv", header=["count"])
python_jobs.to_csv(output_dir/"python_jobs.csv", index=False)
skill_counts_df.to_csv(output_dir/"python_skills.csv",index=False)

total_jobs = len(df)
python_job_count = len(python_jobs)
data_analysis_job_count = len(data_analyze_jobs)

top_skill = skill_counts_df.iloc[0]
top_data_analysis_skill = data_analyze_skill_counts.iloc[0]
top_city = city_salary_sorted.iloc[0]
top_job = high_salary_jobs.iloc[0]

summary_path = output_dir/"job_analysis_summary.txt"

with open(summary_path, "w", encoding="utf-8") as f:
    f.write("Job Analysis Summary\n")
    f.write("====================\n\n")

    f.write(f"Total jobs: {total_jobs}\n")
    f.write(f"Python-related jobs: {python_job_count}\n")
    f.write(f"Data analysis jobs: {data_analysis_job_count}\n\n")

    f.write(
        f"Most frequent skill: {top_skill['skill']} "
        f"({top_skill['count']} times)\n"
    )

    f.write(
        f"Most frequent skill in data analysis jobs: "
        f"{top_data_analysis_skill['skill']} "
        f"({top_data_analysis_skill['count']} times)\n"
    )

    f.write(
        f"City with highest average salary: "
        f"{top_city['city']} "
        f"({top_city['avg_salary']:.2f})\n"
    )

    f.write(
        f"Highest salary job: "
        f"{top_job['title']} in {top_job['city']} "
        f"({top_job['salary']})\n"
    )

print(f"\nSummary saved to {summary_path}")