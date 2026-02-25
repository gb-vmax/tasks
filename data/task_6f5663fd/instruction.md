A machine learning engineer has a text dataset in the file <code>/home/user/data/raw_text.txt</code>. Each line in this file contains a sentence. Your task is to automate the data preparation step by writing a shell script named <code>/home/user/scripts/prepare_data.sh</code> which does the following:

1. Reads <code>/home/user/data/raw_text.txt</code> line by line, converts each sentence to lowercase, removes leading and trailing whitespace, and writes the results to <code>/home/user/data/prepared_text.txt</code>. 
2. After running the script once, the file <code>/home/user/data/prepared_text.txt</code> should exist and contain each sentence from <code>/home/user/data/raw_text.txt</code> in lowercase, trimmed of leading/trailing whitespace, and separated by a newline, preserving the original order. Lines that are completely empty or only whitespace in the source file should result in empty lines in the output as well.
3. After creating the script, execute it and ensure <code>/home/user/data/prepared_text.txt</code> is created with the correctly transformed content.

For final verification, list the contents of the <code>/home/user/data/</code> directory and display the content of <code>/home/user/data/prepared_text.txt</code>. The automated test will compare the output file exactly as specified above.
