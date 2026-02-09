# Bug Report

### Describe the bug

I'm experiencing an issue where string values are no longer being recognized as valid input. After a recent update, the system seems to be rejecting string content that was previously working fine.

### Reproduction

```js
// This used to work but now fails
const content = "# Hello World\n\nThis is a test.";
processor.process(content);

// Only numeric values seem to be accepted now
const numericContent = 12345;
processor.process(numericContent); // This works but shouldn't
```

### Expected behavior

String values should be accepted as valid input, just like before. The processor should handle markdown content passed as strings without any issues.

### Additional context

This appears to have started happening recently. String inputs that were previously processed correctly are now being rejected or causing unexpected behavior. It seems like the validation logic might have changed to only accept numbers, which doesn't make sense for text processing.

---
Repository: /testbed
