# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where character classification seems to be broken. Text that should be treated as punctuation or whitespace is being incorrectly classified, which causes rendering problems in my markdown content.

### Reproduction

```js
// When parsing markdown with punctuation marks
const markdown = `
Hello, world! This is a test.
- List item with punctuation:
- Another item;
`;

// The parser incorrectly classifies characters
// Punctuation marks and whitespace aren't being handled properly
// This affects list rendering and inline formatting
```

### Expected behavior

Punctuation characters should be classified correctly and whitespace/line endings should be distinguished from regular content. The markdown parser should properly identify:
- Whitespace characters (spaces, tabs, line endings)
- Punctuation marks (commas, periods, colons, semicolons, etc.)
- Regular text content

Currently, the classification logic appears to be mixing these categories, leading to incorrect parsing behavior.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
