# Bug Report

### Describe the bug

After a recent update, paragraph nodes in markdown parsing are being created with incorrect type and structure. The paragraph nodes now have `type: "paragraph2"` instead of `type: "paragraph"`, and the `children` property is set to `null` instead of an empty array `[]`.

This breaks any code that relies on the standard paragraph node structure and causes issues when trying to traverse or manipulate the AST.

### Reproduction

```js
const remark = require('remark');

const processor = remark();
const tree = processor.parse('This is a paragraph');

console.log(tree.children[0]);
// Expected: { type: 'paragraph', children: [...] }
// Actual: { type: 'paragraph2', children: null }
```

When parsing markdown with paragraphs, the resulting AST nodes have the wrong type identifier and null children instead of an array.

### Expected behavior

Paragraph nodes should have:
- `type: "paragraph"` (not "paragraph2")
- `children: []` (an array, not null)

This is the standard structure for paragraph nodes in the unified/remark ecosystem and changing it breaks compatibility with existing plugins and transformers.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
