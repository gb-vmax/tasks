# Bug Report

### Describe the bug

I'm encountering an issue with unicode whitespace checking in the markdown parser. When processing certain character codes, the parser seems to be treating `null` values differently than before, which is causing unexpected behavior when parsing markdown content.

### Reproduction

```js
// This used to work correctly but now fails
const result = processor.parse('Some text with   multiple spaces');

// Also having issues with special characters
const result2 = processor.parse('Text\u0000with null character');
```

The parser now seems to handle null character codes (`\u0000`) incorrectly - they're being processed when they should probably be ignored or handled specially.

### Expected behavior

The markdown parser should correctly handle null character codes and distinguish them from undefined values. Previously, null characters were being filtered out properly during whitespace checking, but now they seem to pass through the validation.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
