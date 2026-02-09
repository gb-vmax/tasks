# Bug Report

### Describe the bug
I'm experiencing an issue with markdown parsing where content appears to be getting cut off or not processed correctly. It seems like the parser is returning early when it shouldn't, causing incomplete parsing results.

### Reproduction
```js
const remark = require('remark');

const markdown = `
# Heading

Some content here with multiple paragraphs.

Another paragraph that should be parsed.
`;

const result = remark.parse(markdown);
// Expected: Full AST with all content
// Actual: Incomplete AST, missing some nodes
```

When parsing markdown with multiple sections, the parser seems to stop processing prematurely and returns an incomplete abstract syntax tree. This is particularly noticeable with longer documents or when there are multiple paragraphs/sections.

### Expected behavior
The parser should process the entire markdown input and return a complete AST representing all the content, not just the initial portions.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
