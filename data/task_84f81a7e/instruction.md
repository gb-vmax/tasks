You are a localization engineer tasked with updating and verifying translations for a multilingual web service. In the /home/user/localization directory, you will find three JSON translation files: en.json, fr.json, and de.json. Your job is to update all three translations in parallel based on the following requirements:

1. In each file, add a new key "logout_message" with values:
   - English (en.json): "You have been logged out successfully."
   - French (fr.json): "Vous avez été déconnecté avec succès."
   - German (de.json): "Sie wurden erfolgreich abgemeldet."

2. After updating the translation files, create a verification log named /home/user/localization/update_verification.log containing the following status report:
   - The log should be in YAML format.
   - It must contain for each language (en, fr, de):
     - The language code.
     - Whether the "logout_message" key exists (true/false).
     - The exact value of the "logout_message" key.

Example log format:
en:
  exists: true
  value: "You have been logged out successfully."
fr:
  exists: true
  value: "Vous avez été déconnecté avec succès."
de:
  exists: true
  value: "Sie wurden erfolgreich abgemeldet."

Make sure the formatting of update_verification.log exactly matches the above sample, including indentation and structure. Do not include any additional keys or comments. Only output a summary to the console – all verification must be in the log file.
