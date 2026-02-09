# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX where the content inside code blocks is not being parsed correctly. After processing, the code block content appears to be truncated or only shows the first character/line instead of the full content.

### Reproduction

```mdx
```js
const greeting = 'Hello World';
console.log(greeting);
```
```

When this is processed, only the first character or line of the code block is captured, and the rest of the content is lost or not properly tokenized.

### Expected behavior

The entire content of the fenced code block should be tokenized and preserved. All lines within the code fence should be captured and processed correctly, not just the first character or line.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

This seems to have started happening recently. The code block parsing was working fine before but now it's cutting off the content prematurely.

---
Repository: /testbed
