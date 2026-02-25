You are working as a machine learning engineer preparing a dataset for a text classification project. You have a file located at <code>/home/user/data/training_text.txt</code> that contains one word per line, and some words may appear multiple times. 

Your task is to create a new word frequency report file at <code>/home/user/data/word_frequency_report.txt</code>, which must list every unique word found in <code>training_text.txt</code> along with how many times it appeared. Each line in the report should be in the format:

<pre>
frequency_count word
</pre>

The words must be listed in alphabetical (lexicographical) order. Each frequency_count and word pair should be separated by a single space, and there should be no leading or trailing whitespace. For instance, if the file contains the words “cat”, “dog”, “cat”, and “bird” (each on their own line), your report should look like:

<pre>
1 bird
2 cat
1 dog
</pre>

Make sure to process the file so that the output format is exactly as specified for every unique word. Do not include any extra lines or characters in the output. Save the final report at <code>/home/user/data/word_frequency_report.txt</code>.
