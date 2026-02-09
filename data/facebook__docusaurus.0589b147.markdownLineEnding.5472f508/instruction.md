# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where line endings are not being detected correctly. It seems like certain line breaks in markdown content are being treated as regular characters instead of proper line endings, which causes the parser to fail or produce incorrect output.

### Reproduction

```js
const markdown = `
First line
Second line
Third line
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// Line endings are not recognized properly
// The parser treats newlines as regular content
```

When I try to parse markdown with newlines, the line ending detection logic doesn't work as expected. The function `markdownLineEnding` appears to be returning incorrect results for certain character codes.

### Expected behavior

The parser should correctly identify line endings (newlines, carriage returns, etc.) and treat them as markdown line breaks. Each line should be parsed as a separate block element.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to be a regression as it was working fine in previous versions. Any help would be appreciated!

---
Repository: /testbed
