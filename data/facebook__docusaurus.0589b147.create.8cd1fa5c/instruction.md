# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when parsing markdown content. The parser seems to be calling itself recursively without a proper base case, which causes the application to hang or crash with a stack overflow error.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Test heading

Some paragraph text here.
`;

// This causes infinite recursion
const result = remark.parse(markdown);
```

### Expected behavior

The markdown should be parsed successfully and return an AST without any recursion errors. The parser should complete in a reasonable amount of time.

### System Info

- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. Previously the same markdown content would parse without issues. The stack trace shows the tokenizer creation function being called repeatedly until the call stack is exceeded.

---
Repository: /testbed
