# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where character classification appears to be broken. Text that should be treated as punctuation or whitespace is being misclassified, causing formatting issues in the rendered output.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

// Parse markdown with punctuation and whitespace
const result = processor.processSync('Hello, world! This is a test.');

// The output formatting is incorrect - punctuation and spaces
// are not being handled properly
console.log(result);
```

When parsing markdown content that contains punctuation marks followed by spaces or other whitespace characters, the parser seems to incorrectly classify these characters. This leads to unexpected rendering behavior where:

- Punctuation marks may not be recognized correctly
- Whitespace handling becomes inconsistent
- The overall structure of the parsed content is affected

### Expected behavior

The parser should correctly distinguish between:
1. Whitespace characters (null, line endings, spaces, unicode whitespace)
2. Punctuation characters
3. Regular text characters

Each character type should be classified independently and handled according to markdown specification.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have started happening recently and is affecting any markdown content with mixed punctuation and whitespace.

---
Repository: /testbed
