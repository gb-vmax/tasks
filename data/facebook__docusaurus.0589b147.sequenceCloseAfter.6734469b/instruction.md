# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where the closing fence is not being properly recognized. After recent changes, code blocks that should be closed are either not closing correctly or are behaving unexpectedly.

### Reproduction

```markdown
```js
const foo = 'bar';
```
```

When parsing the above MDX content, the code fence doesn't close properly. The closing backticks should terminate the code block, but it seems like the parser is not recognizing them correctly.

### Expected behavior

The parser should properly recognize and close fenced code blocks when it encounters the closing fence sequence (three or more backticks). The code block should be terminated when the closing fence is followed by either:
- End of file (null)
- A line ending

### Additional context

This appears to affect code blocks regardless of the language specified. The issue manifests when the closing fence is immediately followed by certain characters or end-of-file conditions.

---
Repository: /testbed
