# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where nested elements are being rendered in the wrong order. It seems like buffered content is appearing at the beginning of the output instead of where it should be in the document structure.

### Reproduction

```js
const remark = require('remark');
const html = require('remark-html');

const markdown = `
# Title

Some text with **bold** and *italic*.

- List item 1
- List item 2
`;

const result = remark()
  .use(html)
  .processSync(markdown);

console.log(result.toString());
```

When processing markdown with nested formatting or list structures, the output order is incorrect. Elements that should appear later in the document are showing up at the beginning.

### Expected behavior

The parsed markdown should maintain the correct document order, with buffered fragments appearing in their proper position within the AST hierarchy.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
