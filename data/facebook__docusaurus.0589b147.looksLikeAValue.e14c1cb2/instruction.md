# Bug Report

### Describe the bug

I'm experiencing an issue where string values are no longer being recognized as valid input. After a recent update, the parser is rejecting string content that previously worked fine.

### Reproduction

```js
const content = "# Hello World\n\nThis is a test.";
// Process the content
processor.process(content);
```

When passing a string directly, it's now being treated as invalid input. The same code worked in previous versions.

### Expected behavior

String values should be accepted as valid input for processing. Both strings and Uint8Array buffers should be supported as documented.

### Additional context

This appears to have started happening recently. I haven't changed my code, but the behavior is now different. The parser should accept string input without issues.

---
Repository: /testbed
