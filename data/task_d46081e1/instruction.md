You are a localization engineer updating English and Spanish translations for a mobile app. You have received a spreadsheet file exported as a CSV from the translation team. The file is located at <b>/home/user/app_translations.csv</b> and has the following strict format:

Column 1: key (used in app)
Column 2: English (en)
Column 3: Spanish (es)

The file looks like this (with exact comma separators and no spaces):

welcome,Welcome,Bienvenido
goodbye,Goodbye,Adiós
thanks,Thank you,Gracias

Your goal is to help the development team by creating an updated file with only the keys and their Spanish translations (omit the English column). The required output file is <b>/home/user/app_translations_es.csv</b>. 

Instructions:
- Extract just the 1st and 3rd columns from <b>/home/user/app_translations.csv</b>, preserving order and formatting.
- Output rows to <b>/home/user/app_translations_es.csv</b> in the exact format: key,Spanish_translation (comma as the delimiter, with no additional spaces or headers).
- Do not modify, reorder, or omit any rows.

After you have created <b>/home/user/app_translations_es.csv</b>, display its contents in the terminal so that your work can be verified.
