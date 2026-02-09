# Bug Report

### Describe the bug

I'm encountering an issue with table parsing in GFM (GitHub Flavored Markdown). When a malformed table is provided, the parser seems to hang or behave unexpectedly instead of properly rejecting the invalid syntax.

### Reproduction

```js
const markdown = `
| Header |
| ------ |
| Invalid table with missing delimiter
`;

// Parser doesn't properly handle the malformed table
const result = parse(markdown);
```

The parser should reject tables that don't follow proper GFM table syntax, but it appears to get stuck or not properly call the rejection callback.

### Expected behavior

When encountering an invalid table structure, the parser should cleanly reject it and continue processing the rest of the document. The rejection callback should be invoked with the appropriate code parameter to allow proper error handling.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
