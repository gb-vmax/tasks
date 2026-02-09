# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in markdown content. When processing markdown with leading spaces before blank lines, the parser is not handling them correctly. It seems like the logic for detecting and processing whitespace at the start of blank lines has been inverted.

### Reproduction

```js
const markdown = `
Some text

    

More text
`;

// Parse the markdown
const result = remark.parse(markdown);
```

When there are spaces before a blank line (like indented blank lines), the parser fails to recognize them properly. The whitespace handling appears to be backwards - it's treating lines with spaces as if they don't have spaces, and vice versa.

### Expected behavior

Blank lines with leading whitespace should be parsed correctly. The `linePrefix` should be properly extracted when spaces are present at the beginning of blank lines, and blank lines without leading spaces should be handled as regular blank lines.

### System Info
- remark version: 15.0.1
- Node version: Latest

This is causing issues when parsing markdown documents that have indented blank lines or mixed whitespace patterns.

---
Repository: /testbed
