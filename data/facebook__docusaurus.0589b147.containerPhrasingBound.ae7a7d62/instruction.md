# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where phrasing content inside containers is not being handled correctly. It seems like the parser is not properly recognizing or processing inline elements within block-level containers.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
**bold text** inside a paragraph
`;

const result = processor.parse(markdown);
// The AST structure appears incorrect for phrasing content
```

When parsing markdown with inline/phrasing elements (like bold, italic, links, etc.) nested within container elements (paragraphs, list items, etc.), the resulting AST doesn't match what's expected. The parent-child relationships seem to be inverted or undefined in some cases.

### Expected behavior

The parser should correctly identify phrasing content boundaries within container elements and produce a proper AST with the correct parent-child relationships. Inline elements should be properly nested within their container parents.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
