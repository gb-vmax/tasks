# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the parser seems to hang or fail to properly close/exit certain block elements. After some recent changes, documents that previously parsed correctly are now not being processed properly.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Heading

Some content here

- List item 1
- List item 2

More content
`;

const result = processor.processSync(markdown);
console.log(result);
```

When running this code, the parser doesn't seem to properly handle the closing of elements. The AST appears incomplete or malformed.

### Expected behavior

The markdown should be parsed completely with all elements properly closed and the AST structure should be valid. Previously this same code worked without issues.

### System Info
- remark version: 15.0.1
- Node version: 18.x

Has anyone else encountered this? It seems like something changed in how block elements are being closed during parsing.

---
Repository: /testbed
