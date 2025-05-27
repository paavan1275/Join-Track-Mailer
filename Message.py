def generate_message_with_linkedin(row):
    if pd.notna(row['first_name']) and row['first_name'].strip():
        name = row['first_name']
    elif pd.notna(row['name']) and row['name'].strip():
        name = row['name'].split()[0]
    else:
        name = "there"

    job_title = row['job_title'] if pd.notna(row['job_title']) and row['job_title'].strip() else "professional"
    
    joined = row['has_joined_event']
    
    linkedin_incomplete = row['linkedin_incomplete']
    
    if joined:
        message = (
            f"Hey {name}, thanks for joining our session! "
            f"As a {job_title.lower()}, we think you'll love our upcoming AI workflow tools. "
            "Want early access?"
        )
    else:
        message = (
            f"Hi {name}, sorry we missed you at the last event! "
            f"We're preparing another session that might better suit your interests as a {job_title.lower()}."
        )

    if linkedin_incomplete:
        message += " Also, we noticed your LinkedIn profile is missing—mind adding it to stay updated on relevant opportunities?"

    return message

df_cleaned['message'] = df_cleaned.apply(generate_message_with_linkedin, axis=1)

df_messages = df_cleaned[['email', 'message']]
df_messages.to_csv("Personalized_Messages.csv", index=False)
