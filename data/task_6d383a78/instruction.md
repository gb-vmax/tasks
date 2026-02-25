You are a technical writer tasked with organizing a set of markdown documentation files located under <code>/home/user/docs</code>. Your goal is to generate a plain text summary file at <code>/home/user/doc_summary.txt</code> that lists, one per line, the base name (filename without the path or <code>.md</code> extension) of each <code>.md</code> file found anywhere under <code>/home/user/docs</code> and its subdirectories. The lines in <code>doc_summary.txt</code> should be sorted in ascending (alphabetical) order. Do not include duplicate entries in the summary file even if two files have the same base name in different directories.

Ensure that <code>doc_summary.txt</code> matches the following precise output format:
<ul>
  <li>Each line contains only the base name of a markdown file (e.g., 'introduction', not 'docs/intro.md').</li>
  <li>Each base name appears at most once.</li>
  <li>Lines are sorted in ascending order with no blank lines before, between, or after entries.</li>
</ul>

After you have completed this, print the contents of <code>/home/user/doc_summary.txt</code> to the console so I can verify the output.
