# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the parser crashes when encountering certain edge cases with null/undefined values. The parser seems to be attempting operations on null values that should have been handled earlier.

### Reproduction

```js
// Parsing markdown with specific null/undefined edge cases
const processor = remark();
const result = processor.processSync(someMarkdownContent);
```

When processing certain markdown content, the parser enters an invalid state and tries to call methods on null values, causing unexpected behavior or crashes.

### Expected behavior

The parser should gracefully handle null/undefined values and continue processing without errors. It should properly check for null values before attempting to consume them or perform operations.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to be related to how the text tokenizer handles end-of-input scenarios. The issue appears intermittently depending on the specific markdown content being parsed.

---
Repository: /testbed
