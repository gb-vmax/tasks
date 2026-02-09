# Bug Report

### Describe the bug

I'm experiencing an infinite loop when parsing certain MDX content. The parser seems to get stuck and never completes, causing the application to hang.

### Reproduction

```js
// Parsing this MDX content causes the parser to hang indefinitely
const mdxContent = `
# Hello

Some content here
`;

const result = await compile(mdxContent);
// Never completes - process hangs
```

### Expected behavior

The MDX content should parse successfully and return the compiled result without hanging. The parser should handle null/end-of-content markers properly and exit gracefully.

### Additional context

This appears to affect basic MDX documents. The parser enters an infinite loop and never returns control. I have to manually kill the process.

---
Repository: /testbed
