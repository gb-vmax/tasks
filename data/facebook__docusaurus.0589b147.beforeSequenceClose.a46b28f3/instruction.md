# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When I try to use code fences with backticks or tildes, the closing fence is not being recognized properly, causing the entire rest of the document to be treated as part of the code block.

### Reproduction

```markdown
\```javascript
const x = 1;
\```

This text should be outside the code block but gets included in it.
```

When parsing the above markdown, everything after the opening fence (including the closing fence and subsequent content) is being treated as code content instead of properly closing the code block.

### Expected behavior

The parser should recognize the closing fence sequence and properly terminate the code block. Content after the closing fence should be parsed as normal markdown content, not as part of the code block.

### Additional context

This seems to affect both backtick and tilde fenced code blocks. The opening fence is detected correctly, but the closing fence matching logic appears to be broken. The code block just continues indefinitely until the end of the document.

---
Repository: /testbed
