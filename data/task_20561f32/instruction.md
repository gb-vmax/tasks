I have an old Python utility script at `/home/user/utils/word_freq.py` that I wrote a while back. It reads a text file and prints a word frequency report to stdout. I need to run it against a sample input file and save the output to a report file.

The script takes a single argument: the path to a text file to analyze. It prints word frequencies to stdout, one word per line, in the format:

```
<word>: <count>
```

Words are lowercased, sorted alphabetically, and punctuation is stripped. The output ends with a blank line followed by a summary line in the format:

```
total unique words: <N>
```

Here's what I need you to do:

1. Make the script at `/home/user/utils/word_freq.py` executable (it currently isn't).

2. Run the script with `/home/user/utils/sample.txt` as the input, and redirect its output to `/home/user/utils/report.txt`.

The final file `/home/user/utils/report.txt` should contain the word frequency output produced by the script. Please make sure the file exists and contains the correct output before finishing.
