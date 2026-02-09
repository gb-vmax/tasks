# Bug Report

### Describe the bug

I'm encountering an issue with markdown link/image title parsing. When using single quotes (`'`) for titles in markdown links or images, they're not being recognized correctly. The parser seems to be treating ampersands (`&`) as valid title delimiters instead of single quotes.

### Reproduction

```markdown
[link text](url 'title in single quotes')
![alt text](image.png 'image title')
```

The titles enclosed in single quotes are not being parsed properly. It appears the parser is expecting an ampersand character instead of the single quote.

### Expected behavior

Single quotes should be valid delimiters for link/image titles in markdown, just like double quotes. The parser should correctly recognize and extract titles wrapped in single quotes.

### Additional context

This seems to affect both links and images. Double quotes and parentheses might still work, but single quotes specifically are broken.

---
Repository: /testbed
