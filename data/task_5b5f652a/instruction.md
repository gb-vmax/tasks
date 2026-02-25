A localization engineer needs to update a set of language environment variables for a Python application and document the currently active localization settings. 

1. In the directory /home/user/localization_project/, you will find a file named .env.example containing the following variables:
```
LANG=en_US
LANGUAGE=en
LC_ALL=en_US.UTF-8
```

2. Copy .env.example to create a new .env file in /home/user/localization_project/. Then update the variables in .env so that:
- LANG is set to 'fr_FR'
- LANGUAGE is set to 'fr'
- LC_ALL is set to 'fr_FR.UTF-8'

3. After editing the .env file, export these environment variables into your current terminal session so that they override any existing values.

4. Create a file named locale_status.log in /home/user/localization_project/. Write exactly three lines in this file, with the following fixed format (replace the [...] parts with the values set above):
```
Current LANG: [value_of_LANG]
Current LANGUAGE: [value_of_LANGUAGE]
Current LC_ALL: [value_of_LC_ALL]
```
For example, if you set LANG to fr_FR, the first line must read exactly: "Current LANG: fr_FR" (without quotes). The log file should contain no empty lines and only these three lines.

Your task is complete when locale_status.log exists with the required contents reflecting the updated environment.
