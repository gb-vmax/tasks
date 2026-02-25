You are working as a localization engineer responsible for updating application translations. In the directory /home/user/localization, you will find an English source file named en.txt and a French translation file named fr.txt. Your task is to update the French translation based on the latest entries from en.txt. Only untranslated entries (lines where the French translation is missing) should be appended to fr.txt with an empty translation, using the format: key= (the key followed by an equal sign and nothing after it).

For example, if en.txt contains:
greeting=Hello
farewell=Goodbye

and fr.txt contains:
greeting=Bonjour

then after updating, fr.txt should look like:
greeting=Bonjour
farewell=

If fr.txt is missing or has incorrect permissions, create it with the missing entries and use the format described above.

To confirm your work, create a log file at /home/user/localization/update_log.txt listing one line per newly added entry (if any), in the format: Added missing translation: key, where "key" is the actual key from en.txt.

If there are no missing translations to add, write No missing translations found. in the log file.

Ensure all files are writable by the 'user' account.
