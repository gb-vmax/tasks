# Bug Report

### Describe the bug

I'm encountering an issue with string extraction from AST buffers when using Node.js Buffer objects. The extracted strings appear to be truncated or contain incorrect characters, especially for strings that have multi-byte UTF-8 characters or longer content.

### Reproduction

```js
// Create an AST buffer with a string
const buffer = Buffer.from(/* some AST data with strings */);
const ast = getAstBuffer(buffer);

// Try to extract a string from the buffer
const extractedString = ast.convertString(position);

// The string is cut off or contains garbage characters
console.log(extractedString); // Expected: "Hello World", Actual: "Hell"
```

### Expected behavior

Strings should be fully extracted from the buffer with correct UTF-8 decoding, regardless of their length or character composition. The byte range calculation should properly account for the string length to read the complete content.

### System Info
- Node.js version: 18.x
- Running on: Linux

---
Repository: /testbed
