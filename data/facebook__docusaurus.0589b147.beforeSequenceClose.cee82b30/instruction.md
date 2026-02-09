# Bug Report

### Describe the bug
Code fences in MDX are not being parsed correctly. When I try to use fenced code blocks with backticks, the closing fence is not recognized properly and the code block doesn't close as expected.

### Reproduction
```mdx
```js
const example = "test";
```
```

The code block above doesn't parse correctly - the closing fence is ignored and the rest of the document gets treated as part of the code block.

### Expected behavior
The closing fence (```) should properly close the code block and allow the rest of the MDX content to be parsed normally. The opening and closing fences should match and delimit the code block correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
