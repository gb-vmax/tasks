You are organizing a set of documentation files as a technical writer. In the directory <code>/home/user/docs/</code>, you have a JSON file named <code>articles.json</code> that contains an array of article metadata. Your goal is to ensure the file follows a specific schema and to extract a concise summary.

1. Validate that <code>/home/user/docs/articles.json</code> conforms to this schema:
    - The top-level object must have a property <code>articles</code>, which is an array.
    - Each item in <code>articles</code> must be an object containing these fields:
        - <code>id</code>: integer
        - <code>title</code>: string
        - <code>author</code>: string
        - <code>published</code>: boolean

2. After confirming schema conformity, extract a list of article titles and authors only, and output this as a new JSON file named <code>/home/user/docs/article_summaries.json</code>.

The required format of <code>article_summaries.json</code> is:
<pre>
[
  {"title": "Title1", "author": "Author1"},
  {"title": "Title2", "author": "Author2"}
  ...
]
</pre>
If schema validation fails, do not create <code>article_summaries.json</code> and instead record "INVALID SCHEMA" inside <code>/home/user/docs/validation.log</code>. If validation succeeds, write "SCHEMA VALID" in <code>validation.log</code> and generate the summary file as specified above.
