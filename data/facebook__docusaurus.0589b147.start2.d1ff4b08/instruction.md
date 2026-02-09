# Bug Report

### Describe the bug

The parser appears to hang indefinitely when processing ATX-style headings (headings that start with `#`). The application becomes completely unresponsive and eventually crashes with a stack overflow or timeout error.

### Reproduction

```js
const mdx = require('@mdx-js/mdx');

const content = `
# Heading 1
Some content here
`;

// This call never completes and causes the process to hang
await mdx.compile(content);
```

### Expected behavior

The MDX content should parse successfully and return the compiled output. ATX headings are a standard markdown feature and should be handled without any issues.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: 18.x

This seems to have started happening recently. Any markdown file with headings causes the parser to freeze. Let me know if you need any additional information!

---
Repository: /testbed
