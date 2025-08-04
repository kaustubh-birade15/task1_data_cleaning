# First Task: Preprocessing and Data Cleaning

 ## The goal
 By handling missing values, eliminating duplicates, standardizing formats, and getting the data ready for additional analysis, this task aimed to clean and preprocess a raw dataset.


 ---

 ## 📁 Dataset Employed ** Netflix Movies and TV Series Dataset Name: **Source:**  [Kaggle: Netflix TV Series and Films] (https://www.kaggle.com/datasets/shivamb/netflix-shows)

 ---

 ## Tools & Technologies: VS Code, Pandas, Python 3.11

 ---

 ## Cleaning Procedures Followed

 The dataset was loaded using `pandas.read_csv()`.
 Using `drop_duplicates()`, duplicate records were eliminated.
 3. **Used forward fill to handle missing values** (`fillna(method='ffill')`).
 4. **Normal column names**:
    Changed to lowercase
    Leading and trailing spaces were eliminated.
    Substituted underscores for spaces
 5. **Used `pd.to_datetime()` to convert `date_added` column** to consistent datetime format.

 ---

 ## 📦 Included Files | File Name | Description | ----------------------| ------------------------------------------------------ || `netflix_titles.csv` | Original raw dataset || `cleaned_dataset.csv`| The dataset's final cleaned version || `clean_data.py` | Python script used for data preprocessing |

 ---

 ## ✅ Output
 `cleaned_dataset.csv`, the cleaned dataset, is now:
 Duplicate-free, format-consistent, and prepared for additional analysis, visualization, or modeling tasks

 ---

 ## 👨‍💻 Author: Kaustubh Birade Data Analyst Internship: Submission of Task 1