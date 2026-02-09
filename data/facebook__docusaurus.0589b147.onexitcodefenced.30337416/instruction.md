# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX where trailing newlines are not being properly removed from the code block content. This causes the rendered output to include unexpected blank lines at the end of code blocks.

### Reproduction

```mdx
```js
const example = 'hello';
console.log(example);
```
```

When this is processed, the code block value includes a trailing newline that should have been stripped out. The expected behavior is that both leading AND trailing newlines should be removed from fenced code blocks.

### Expected behavior

Fenced code blocks should have both their leading and trailing newlines removed during parsing, similar to how they were handled previously. The final code block value should be clean without extra whitespace at the beginning or end.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
