# Bug Report

### Describe the bug

I'm experiencing an issue with text serialization where tab characters are not being handled correctly. When processing chunks that contain tabs, the output is missing characters or producing incorrect results.

### Reproduction

```js
// Processing text with tabs
const chunks = ['Hello', -2, 'World'];
const result = serializeChunks2(chunks, true);

// Expected: "Hello\tWorld" 
// Actual: Missing first character or incorrect tab handling
```

The problem occurs when:
1. Processing an array of text chunks that includes tab characters (represented as -2)
2. Using the `serializeChunks2` function with tab expansion enabled
3. The first chunk or characters after tabs are not being processed correctly

### Expected behavior

The function should correctly serialize all chunks including tab characters, and no characters should be skipped or lost during processing.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
