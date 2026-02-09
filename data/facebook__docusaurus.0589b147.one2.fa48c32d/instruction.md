# Bug Report

### Describe the bug

I'm experiencing an issue with the remark parser where it seems to fail silently when processing certain markdown structures. The parser doesn't throw any errors or warnings, but it also doesn't produce the expected output for valid markdown input.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Heading

Some paragraph text.

- List item 1
- List item 2
`;

const result = processor.processSync(markdown);
console.log(result); // Expected AST is not generated correctly
```

When processing markdown with nested structures or custom node types, the parser seems to skip over certain elements without any indication that something went wrong.

### Expected behavior

The parser should either:
1. Successfully parse the markdown and generate the complete AST
2. Throw an error or warning if it encounters something it can't handle

Instead, it appears to be silently failing for certain node types, making it difficult to debug what's going wrong.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

Has anyone else encountered this? It seems like the parser might be checking the wrong property or condition when determining how to handle certain nodes.

---
Repository: /testbed
