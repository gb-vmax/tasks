# Bug Report

### Describe the bug

After a recent update, markdown links are not being parsed correctly. The link syntax `[text](url)` is not recognized and remains as plain text in the output.

### Reproduction

```markdown
This is a [link](https://example.com) that should work.
```

Expected output: A properly formatted link
Actual output: The raw markdown text is displayed without being converted to a link

### Steps to reproduce
1. Create a markdown file with link syntax
2. Process it through the MDX parser
3. The link markers are not properly closed/processed

This seems to have started happening recently. Links were working fine before but now they're just showing up as plain text in the rendered output.

### System Info
- MDX version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
