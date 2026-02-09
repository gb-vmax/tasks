# Bug Report

### Describe the bug
When rendering strong/bold text (using `**text**` or `__text__` syntax), the output is not properly formatted. The closing markers appear to be missing or incorrect, resulting in malformed markdown output.

### Reproduction
```js
// Input markdown with strong text
const markdown = '**bold text**';

// After processing, the output is incorrect
// Expected: **bold text**
// Actual: **bold text*  (missing closing marker)
```

This also affects underscore-style bold text:
```js
const markdown = '__bold text__';
// Similar issue with closing markers
```

### Expected behavior
Strong text should be rendered with proper opening and closing markers (`**` or `__`). The markdown output should maintain the correct syntax for bold formatting.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
