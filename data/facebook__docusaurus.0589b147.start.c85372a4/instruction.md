# Bug Report

### Describe the bug

After a recent update, the markdown parser is throwing errors when processing definition syntax. The parser seems to fail during tokenization of definition blocks, causing the entire parsing process to crash.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
[link]: https://example.com "Example"

This is a [link] to example.
`;

// This now throws an error
const result = processor.processSync(markdown);
```

### Expected behavior

The markdown should parse successfully and definition references should work as before. The parser should tokenize definition blocks without errors.

### Additional context

This appears to have broken after the latest changes to the tokenization logic. The error occurs specifically when the parser encounters definition syntax like `[link]: url "title"`.

---
Repository: /testbed
