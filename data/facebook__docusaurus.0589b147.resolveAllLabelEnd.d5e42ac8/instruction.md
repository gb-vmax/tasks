# Bug Report

### Describe the bug

I'm experiencing an issue with parsing markdown that contains label-like syntax (links/images). It appears that when the parser encounters these elements, they're not being properly converted or removed from the token stream, causing unexpected behavior in the output.

### Reproduction

```js
// Example markdown with image/link labels
const markdown = `
![alt text](image.jpg)
[link text](https://example.com)
`;

// When parsing this markdown, the token processing seems off
// The labelImage and labelLink tokens aren't being handled correctly
```

The problem seems to manifest when the parser tries to resolve label endings. The tokens that should be converted to data tokens or removed from the event stream aren't being processed at the right positions.

### Expected behavior

Label tokens (labelImage, labelLink, labelEnd) should be properly converted to data tokens and the appropriate number of events should be removed from the stream. The markdown should parse correctly without leaving artifacts or malformed token sequences.

### System Info
- remark version: 15.0.1
- Node version: Latest

This might be related to how the event array is being modified during iteration. The splice operation and index adjustment don't seem to be in sync.

---
Repository: /testbed
