import pandas as pd

file_path = r"C:\Users\paava\Downloads\Data.xlsx" 
df = pd.read_excel(file_path)

df_cleaned = df.drop_duplicates()
df_cleaned['has_joined_event'] = df_cleaned['has_joined_event'].map({'Yes': True, 'No': False})

df_cleaned.rename(columns={
    "What is your LinkedIn profile?": "linkedin_profile",
    "Job Title": "job_title"
}, inplace=True)

def is_incomplete_linkedin(url):
    if pd.isna(url):
        return True
    url_str = str(url).strip().lower()
    return not (url_str.startswith("http://") or url_str.startswith("https://") or "linkedin.com/in/" in url_str)

df_cleaned['linkedin_incomplete'] = df_cleaned['linkedin_profile'].apply(is_incomplete_linkedin)

df_cleaned['job_title_missing'] = df_cleaned['job_title'].isna() | (df_cleaned['job_title'].str.strip() == "")

df_cleaned.to_csv("Cleaned_DataSheet1_Renamed.csv", index=False)
