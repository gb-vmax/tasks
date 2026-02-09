# Bug Report

### Describe the bug

I'm experiencing an issue with punctuation detection in markdown parsing. It seems like certain punctuation characters are not being recognized correctly, which causes problems when parsing markdown content that contains mixed ASCII and Unicode punctuation marks.

### Reproduction

```js
// When parsing markdown with punctuation like:
const markdown = `This is a test—with em dash.`;

// Or content with other punctuation:
const content = `Hello! How are you?`;
```

The parser doesn't handle these punctuation marks as expected. Characters that should be treated as punctuation are being ignored or handled incorrectly.

### Expected behavior

Both ASCII punctuation (like `!`, `?`, `.`) and Unicode punctuation (like em dashes `—`, ellipsis `…`, etc.) should be properly recognized as punctuation characters during markdown parsing.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
