# Bug Report

### Describe the bug

I'm experiencing an issue with column position tracking in the markdown tokenizer. When processing markdown content, the column positions seem to be off by one, causing incorrect position information to be reported for tokens.

### Reproduction

```js
const remark = require('remark');
const parser = remark();

const markdown = `
# Header
Some text here
`;

const ast = parser.parse(markdown);

// Check the column positions in the AST
// The column values are offset by 1 from where they should be
console.log(ast.children[0].position);
// Expected: column starts at correct position
// Actual: column is off by 1
```

### Expected behavior

The tokenizer should accurately track column positions for all tokens. Column positions should reflect the actual character positions in the source markdown without any offset errors.

### System Info
- remark version: 15.0.1
- Node version: Latest

This is causing issues with source mapping and error reporting in my markdown processing pipeline. The column positions being off by one makes it difficult to accurately highlight or reference specific parts of the source markdown.

---
Repository: /testbed
