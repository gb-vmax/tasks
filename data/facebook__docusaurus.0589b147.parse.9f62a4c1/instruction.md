# Bug Report

### Describe the bug

I'm experiencing an issue with the `parse` method where it's not correctly passing the processed file object to the parser. After parsing a file, the parser receives the original file input instead of the VFile object that was created.

### Reproduction

```js
const processor = remark();

const file = {
  value: '# Hello',
  path: 'example.md'
};

const result = processor.parse(file);

// The parser receives the original file object instead of the VFile instance
// This causes issues when the parser expects VFile-specific properties
```

### Expected behavior

The parser should receive the `realFile` (VFile instance) that was created from the input, not the original `file` parameter. This ensures that the parser has access to all VFile methods and properties that may have been set during the VFile creation process.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
