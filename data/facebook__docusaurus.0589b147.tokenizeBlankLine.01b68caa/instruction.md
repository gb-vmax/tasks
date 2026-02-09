# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in MDX content. It seems like blank lines are not being recognized correctly, which is causing parsing failures or unexpected behavior in my MDX documents.

### Reproduction

```mdx
# Heading

Some text here

Another paragraph after a blank line
```

When parsing this MDX content, the blank line between paragraphs is not being handled properly. The parser either fails to recognize it as a valid blank line or treats it incorrectly.

### Expected behavior

Blank lines should be properly recognized and parsed in MDX documents. A line containing only whitespace (spaces/tabs) or completely empty should both be treated as valid blank lines that separate content blocks.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
