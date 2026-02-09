# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When a fenced code block has content that starts with spaces, the leading spaces are being incorrectly stripped or handled, causing the indentation to not be preserved as expected.

### Reproduction

```markdown
```js
  const x = 1;
    const y = 2;
```
```

The indentation inside the code block is not being preserved correctly. The spaces at the beginning of each line are being removed or modified.

### Expected behavior

The content inside fenced code blocks should preserve all leading whitespace exactly as written. If I have 2 spaces before `const x = 1;`, those 2 spaces should remain in the parsed output.

### Additional context

This seems to affect code blocks where the content lines have any amount of leading whitespace. The parser appears to be treating the whitespace differently than it should.

---
Repository: /testbed
