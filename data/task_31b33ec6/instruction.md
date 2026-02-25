You are a localization engineer updating translation files for a software project. In your home directory (/home/user), you will find a compressed archive named /home/user/locales_update.tar.gz. This archive contains a directory called locales, which includes updated translation files for various languages (en_US.po, fr_FR.po, de_DE.po). 

Your task is as follows:
1. Extract the locales_update.tar.gz archive into your home directory so that a new directory, /home/user/locales, is created containing the translation files.
2. Once extraction is complete, verify the extraction by listing the contents of the /home/user/locales directory (not recursive), in a simple text file called /home/user/locales_extraction.log. The log file should strictly contain only the file names, one per line, with no additional text, headers, or directories.

The automated test will specifically check that:
- The /home/user/locales directory exists.
- The files en_US.po, fr_FR.po, and de_DE.po exist in /home/user/locales.
- The /home/user/locales_extraction.log file exists and lists exactly the names of the .po files, one per line, with no extra whitespace or information.

Do not modify the contents of the .po files themselves. Focus only on extraction and logging as described above.
