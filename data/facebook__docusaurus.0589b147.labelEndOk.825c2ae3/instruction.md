# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where certain link formats are causing unexpected behavior. It seems like the label end tokenizer is not properly handling the completion of link labels in some edge cases.

### Reproduction

```js
const markdown = `[link text](url)`;
// Process this markdown

// Also happens with reference-style links:
const refLink = `[link][ref]`;
```

When processing markdown with links, the parser appears to be returning incorrect values or getting stuck during the label end tokenization phase. This affects both inline links and reference-style links.

### Expected behavior

Links should be parsed correctly and the tokenizer should properly complete the label end processing without returning unexpected values.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
