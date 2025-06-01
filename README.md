# Personalized Messaging – Suggests a communication bridge between hosts and attendees.

-  Clean and deduplicate event data
-  Normalize and validate fields like `has_joined_event`, job title, LinkedIn profile
-  Flag incomplete or missing profile information
-  Automatically generate tailored outreach messages
-  Export results to a clean CSV file for further use
-  Ready for integration with email clients like Outlook or Gmail via SMTP

---

## 🧠 How It Works

1. Load the cleaned dataset from Excel or CSV
2. For each row:
   - Checks whether the participant joined the event
   - Reads name, job title, and LinkedIn presence
   - Crafts a customized message
3. Outputs a final CSV file with the format:
   ```csv
   email, message
