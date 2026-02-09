# Bug Report

### Describe the bug

Code fences in MDX are not being parsed correctly. When I try to use fenced code blocks in my MDX files, they're not being recognized properly and the closing fence isn't working as expected.

### Reproduction

```mdx
# My Document

```js
const hello = 'world';
```

More content here
```

The code fence doesn't close properly and the parser seems to be treating the rest of the document as part of the code block.

### Expected behavior

The code fence should close after the closing backticks and the rest of the document should be parsed normally. The closing fence should be recognized when followed by a newline or at the end of the file.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
