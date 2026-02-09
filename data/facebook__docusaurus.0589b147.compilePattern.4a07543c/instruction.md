# Bug Report

### Describe the bug

I'm experiencing an issue with special character escaping in markdown parsing. When using certain characters like hyphens (`-`) or plus signs (`+`) in markdown content, they're being incorrectly escaped or not escaped when they should be, leading to unexpected rendering behavior.

### Reproduction

```js
// Example markdown content that's not being processed correctly
const markdown = `
Some text with a hyphen-separated-word
Another line with a + symbol
`;

// The hyphen and plus characters aren't being handled properly
// during the compilation/parsing phase
```

### Expected behavior

Special characters like `-` and `+` should be properly escaped when they need to be treated as literal characters in regex patterns, but the current logic seems to have an issue with when the escaping is applied versus when the capture group is created.

The pattern compilation should correctly handle these characters based on whether they appear in contexts that require regex escaping.

### System Info
- remark version: 15.0.1
- Node version: Latest LTS

---
Repository: /testbed
