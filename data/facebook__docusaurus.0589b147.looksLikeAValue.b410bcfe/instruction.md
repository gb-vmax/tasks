# Bug Report

### Describe the bug

I'm encountering an issue where string content is not being processed correctly. When passing string values to MDX, they are being rejected even though strings should be valid input.

### Reproduction

```js
// This should work but doesn't
const content = "# Hello World";
const result = compile(content);
// Throws an error or returns unexpected result

// Also fails with regular text
const text = "Some regular text content";
processContent(text);
// String is not recognized as valid input
```

### Expected behavior

String values should be accepted as valid input. Both markdown strings and regular text strings should be processed without errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
