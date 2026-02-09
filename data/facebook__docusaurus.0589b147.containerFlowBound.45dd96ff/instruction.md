# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where container flow elements are not being processed correctly. It seems like the parent-child relationship might be inverted, causing the parser to fail when handling certain block-level markdown structures.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Heading

> This is a blockquote
> with multiple lines

Some text after
`;

const result = remark().parse(markdown);
// The blockquote structure is malformed or throws an error
```

When parsing markdown with container flow elements (like blockquotes, lists, or other block-level containers), the resulting AST has incorrect parent-child relationships or the parsing fails entirely.

### Expected behavior

Container flow elements should be parsed correctly with proper parent-child relationships in the AST. The parser should handle nested block-level elements without errors.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
