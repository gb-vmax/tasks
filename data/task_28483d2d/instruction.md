You are a security auditor who needs to review file access within a project. You are given a CSV file located at <b>/home/user/project/access_report.csv</b> that contains the following columns: <i>username,filename,permission</i>. 

Your task is to parse this CSV file and filter all entries where the <b>permission</b> is not equal to <i>read</i>. Convert only these filtered entries into JSON format and save the result to <b>/home/user/project/non_read_permissions.json</b>.

The JSON output must be an array of objects, where each object has keys <b>username</b>, <b>filename</b>, and <b>permission</b>. The file should be formatted with each object on its own line and no extra whitespace or indentation. For example:

<pre>
[
{"username":"alice","filename":"secret.txt","permission":"write"},
{"username":"bob","filename":"log.txt","permission":"execute"}
]
</pre>

Please ensure the output JSON file matches this exact structure, order, and formatting, with no trailing commas or extra spaces. If there are no non-read permissions, create an empty array: <code>[]</code>.
