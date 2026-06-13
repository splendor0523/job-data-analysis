# Job Data Analysis Project

This is a small pandas project for analyzing job posting data.

## Project Goal

The project reads a CSV file of job postings and generates several analysis results, including:

* Data analysis related jobs
* Python related jobs
* Job counts by city
* Job title frequency
* Skill frequency
* Skill frequency in data analysis jobs
* Average salary by city
* Jobs sorted by salary
* A text summary report

## Project Structure

```text
day6/
├── data/
│   └── jobs.csv
├── output/
├── scripts/
│   └── analyze_jobs.py
├── README.md
└── requirements.txt
```

## Input Data

The input file is:

```text
data/jobs.csv
```

The CSV file contains the following columns:

```text
title, city, salary, skills
```

## How to Run

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis script:

```bash
python scripts/analyze_jobs.py
```

The script can also run from the `scripts` folder because it uses `pathlib.Path` to locate the project directory.

## Outputs

The analysis results are saved in the `output/` folder.

Main output files include:

```text
data_analysis_jobs.csv
python_jobs.csv
city_counts.csv
title_counts.csv
skill_counts.csv
data_analysis_skill_counts.csv
city_avg_salary.csv
city_avg_salary_sorted.csv
high_salary_jobs.csv
job_analysis_summary.txt
```

## Key Skills Practiced

This project practices:

* Reading CSV files with pandas
* Filtering rows with `str.contains()`
* Counting values with `value_counts()`
* Splitting multi-value text with `str.split()`
* Expanding list-like cells with `explode()`
* Grouping data with `groupby()`
* Sorting data with `sort_values()`
* Exporting CSV files
* Writing text summary files
* Managing project paths with `pathlib.Path`

