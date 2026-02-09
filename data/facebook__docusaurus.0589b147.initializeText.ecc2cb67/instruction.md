# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the parser seems to hang or crash when processing certain text content. The application becomes unresponsive when trying to parse specific markdown documents.

### Reproduction

```js
const markdown = `
This is a test document with some text.

Here's another paragraph with **bold** and *italic* text.
`;

// Parser hangs or crashes when processing this
const result = remark.parse(markdown);
```

The issue appears to happen with various markdown inputs, particularly when there are breaks or transitions between different text constructs. Sometimes the parser just stops responding entirely.

### Expected behavior

The markdown should be parsed successfully without hanging or crashing. The parser should handle text data and construct transitions properly.

### Additional context

This started happening recently and I can't pinpoint exactly what changed. The same markdown content used to parse fine before. It seems related to how the parser handles data exits and transitions between different parsing states.

---
Repository: /testbed
