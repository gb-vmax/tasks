# Bug Report

### Describe the bug

I'm experiencing an issue with markdown line ending detection in the MDX parser. It seems like the parser is not correctly identifying line breaks in certain scenarios, which is causing content to be parsed incorrectly.

### Reproduction

When processing markdown content with specific line ending characters, the parser doesn't recognize them properly:

```js
// Content with newline characters (code 10-12 range)
const content = `# Title
Some text here
Another line`;

// The line endings are not being detected correctly
// This causes the content to be parsed as a single block
// instead of separate lines
```

### Expected behavior

The parser should correctly identify standard line ending characters (newlines, carriage returns, etc.) and parse multi-line content appropriately. Each line should be treated as a separate element when appropriate.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have broken after a recent update. The line ending detection logic might not be handling the full range of newline character codes properly.

---
Repository: /testbed
