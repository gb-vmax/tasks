# Bug Report

### Describe the bug

I'm experiencing a crash when parsing certain markdown content. The parser throws a `TypeError: Cannot read property 'restore' of undefined` error during tokenization.

This seems to happen with specific markdown structures, but I haven't been able to narrow down the exact pattern yet. The error occurs during the parsing phase and prevents the entire document from being processed.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Test Document

Some content here with various markdown elements.
`;

// Parser crashes with TypeError
const result = remark.parse(markdown);
```

### Expected behavior

The markdown should parse successfully without throwing errors. The parser should handle the tokenization process gracefully even when encountering edge cases.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

The error message indicates something is wrong with the `info.restore()` call in the tokenizer, but I'm not sure what's causing `info` to be undefined in certain cases.

---
Repository: /testbed
