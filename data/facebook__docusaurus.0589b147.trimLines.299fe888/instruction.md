# Bug Report

### Describe the bug

I'm experiencing an issue with text trimming in code blocks. It appears that newline characters are being included incorrectly when processing multi-line content, causing extra characters to appear in the output.

### Reproduction

```js
const content = `line one
line two
line three`;

// After processing through trimLines, the output includes
// unexpected newline characters that shouldn't be there
const result = trimLines(content);
// Result has extra characters at line boundaries
```

### Expected behavior

The `trimLines` function should properly trim whitespace from each line without including the newline character itself in the trimmed content. Each line should be processed independently and then joined back together with the original line separators.

Currently getting output that includes the newline as part of the line content instead of as a separator, which breaks formatting in rendered markdown/code blocks.

### System Info
- Version: latest
- Environment: Node.js

---
Repository: /testbed
