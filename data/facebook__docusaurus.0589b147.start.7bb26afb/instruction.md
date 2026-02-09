# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where whitespace handling in certain contexts appears to be broken. The parser seems to be processing spaces incorrectly, which causes the markdown content to not render as expected.

### Reproduction

```js
const markdown = `
[link]: https://example.com "Title with spaces"

Some text here
`;

// Parse the markdown
const result = remark().parse(markdown);

// The definition is not parsed correctly
// Whitespace after line endings is handled incorrectly
```

When parsing markdown with definitions that span multiple lines or have specific whitespace patterns, the output is not what I'd expect. It seems like the whitespace detection logic is inverted or the control flow is wrong.

### Expected behavior

The markdown parser should correctly handle whitespace in definitions and other block elements, properly distinguishing between line prefixes and suffixes. Line endings followed by spaces should be processed in the correct order.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
