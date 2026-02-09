# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. After a recent update, code blocks that should be properly closed are not being recognized correctly. The parser seems to be rejecting valid closing fence sequences.

### Reproduction

```markdown
```js
const x = 1;
```
```

When parsing the above markdown, the code block is not being properly closed. The closing fence (```) should terminate the code block, but it's being treated as invalid.

### Expected behavior

The parser should recognize the closing fence sequence and properly close the code block. Code blocks with valid opening and closing fences should be parsed correctly, regardless of whether they end with a newline or EOF.

### Additional context

This appears to affect code blocks at the end of files or before other markdown elements. The issue manifests when the closing fence is followed by either a newline or EOF - both of these should be valid ways to close a fenced code block.

---
Repository: /testbed
