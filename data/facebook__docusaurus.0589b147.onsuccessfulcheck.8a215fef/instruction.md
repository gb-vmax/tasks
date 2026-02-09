# Bug Report

### Describe the bug

I'm encountering an issue where the markdown parser crashes with a `TypeError` when processing certain markdown constructs. The error occurs when `info.restore()` is called on an undefined or null `info` object during tokenization.

### Reproduction

```js
const remark = require('remark');

// This causes a crash
const result = remark.parse(`
# Heading
Some text with [link](url)
`);
```

The error message is:
```
TypeError: Cannot read property 'restore' of undefined
```

### Expected behavior

The markdown should be parsed successfully without throwing errors. The parser should handle cases where the `info` object might be undefined or missing the `restore` method.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to happen specifically during the tokenization phase when checking successful constructs. The parser worked fine in earlier versions.

---
Repository: /testbed
