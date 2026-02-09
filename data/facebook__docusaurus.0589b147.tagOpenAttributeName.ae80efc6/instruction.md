# Bug Report

### Describe the bug

I'm experiencing an issue with HTML parsing where certain attribute names in HTML tags are being consumed incorrectly. It appears that the parser is consuming characters even when they shouldn't be part of valid attribute names, leading to unexpected parsing behavior.

### Reproduction

```js
// When parsing HTML with specific attribute patterns
const input = `<div attr=value>content</div>`;

// The parser seems to consume characters that shouldn't be part of the attribute name
// This affects how the HTML is tokenized and processed
```

### Expected behavior

The parser should only consume characters that are valid for HTML attribute names (alphanumeric characters, hyphens, periods, colons, and underscores). Characters that don't match this pattern should not be consumed as part of the attribute name and should trigger the transition to the next parsing state.

### System Info
- Version: remark@15.0.1
- Node.js: Latest

The issue seems to be in the HTML text tokenization logic where attribute names are being processed. The order of operations appears to be causing valid characters to be consumed even when they shouldn't be.

---
Repository: /testbed
