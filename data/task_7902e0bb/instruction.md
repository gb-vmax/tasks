As an MLOps engineer, you regularly run machine learning experiments and track their generated artifact filenames in a file for analysis. You have a text file at <code>/home/user/artifact_names.txt</code>. Each line in this file is a single artifact filename, such as <code>model_v1.pt</code>, <code>metrics.json</code>, or <code>training.log</code>. Some filenames appear multiple times, as multiple models may generate artifacts with identical names.

Your goal is to determine how many times each unique artifact filename appears in <code>artifact_names.txt</code> to help analyze artifact generation patterns. You are to generate a report file at <code>/home/user/artifacts_frequency_report.txt</code>.

The required report format is:

<ul>
<li>Each line contains: the artifact filename, followed by a colon and a single space, then the frequency count, e.g.:
<pre>
model_v1.pt: 4
metrics.json: 3
training.log: 2
</pre>
</li>
<li>All filenames must appear only once in the report.</li>
<li>Sort the report by frequency count in descending order (most frequent files first). If two or more filenames have the same count, sort those alphabetically (A-Z).</li>
<li>The report must have <b>no extra spaces or blank lines</b> at the top or bottom.</li>
</ul>

Once you have created the <code>/home/user/artifacts_frequency_report.txt</code> file with the requirements above, please print its contents to the console.
