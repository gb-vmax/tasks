# Bug Report

### Describe the bug

The markdown parser is producing incorrect output when processing certain token sequences. It appears that the serialization logic is applying operations in the wrong order, causing the text content to be corrupted or not properly formatted.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Test heading
Some text with **bold** and *italic* formatting.
`;

const result = remark.parse(markdown);
// The serialized output is malformed
```

When parsing markdown with mixed formatting or special characters, the output doesn't match the expected structure. The token stream seems to be processed incorrectly, leading to garbled text or missing content.

### Expected behavior

The parser should correctly serialize tokens and preserve the original markdown structure. Text content should be properly extracted and formatted according to the token types.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
