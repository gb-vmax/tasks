You are a localization engineer who needs to update and verify translation files for an application. Complete the following steps:

1. In the directory /home/user/localization, you will find two text files:
   - /home/user/localization/source.txt (contains English phrases, one per line)
   - /home/user/localization/old_fr.txt (contains French translations of some phrases from source.txt, in the format "ENGLISH=FRENCH")

2. Your task is to generate a new translation file /home/user/localization/new_fr.txt in the following format:
   - For every line in source.txt:
     * If an English phrase (the entire line) exists in any "ENGLISH=FRENCH" pair in old_fr.txt, copy the "ENGLISH=FRENCH" line exactly to new_fr.txt.
     * If an English phrase does NOT exist in old_fr.txt, append a new entry in new_fr.txt using the format "ENGLISH=", leaving the FRENCH part blank.

3. After generating new_fr.txt, produce a log file at /home/user/localization/update.log containing:
   - For each added blank translation, a line in the format: "MISSING: ENGLISH"
   - For each copied translation, a line in the format: "COPIED: ENGLISH"

4. The order of entries in new_fr.txt and update.log must match the order of phrases in source.txt.

Example:
If source.txt has the lines:
Hello
Exit

and old_fr.txt has:
Hello=Bonjour

then new_fr.txt should contain:
Hello=Bonjour
Exit=

and update.log should contain:
COPIED: Hello
MISSING: Exit

Ensure that new_fr.txt and update.log are present in /home/user/localization, with contents matching the specifications above.
