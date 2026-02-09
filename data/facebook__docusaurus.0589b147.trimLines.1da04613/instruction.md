# Bug Report

### Describe the bug

I'm experiencing an issue with MDX text processing where line breaks and whitespace are being incorrectly trimmed in certain scenarios. It appears that the last character before a newline is being removed when it shouldn't be.

### Reproduction

```mdx
Some text here
Another line
```

When processing this MDX content, the output is missing characters at the end of lines. For example, "here" becomes "her" and similar truncation happens throughout the document.

### Expected behavior

The text should be preserved exactly as written, with only intentional whitespace trimming. No content characters should be removed during the line trimming process.

### Additional context

This seems to affect multi-line MDX documents where newlines are present. Single-line content appears to work fine, but anything with line breaks shows this character truncation issue.

---
Repository: /testbed
