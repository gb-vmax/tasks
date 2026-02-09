# Bug Report

### Describe the bug

I'm experiencing issues with emphasis nodes in markdown parsing. When creating multiple emphasis elements, they seem to be sharing the same children array, causing content from one emphasis node to appear in others. Additionally, the node structure appears corrupted with the `type` property being set incorrectly.

### Reproduction

```js
const remark = require('remark');

const markdown = `
*first emphasis*

*second emphasis*
`;

const tree = remark.parse(markdown);
console.log(tree);
```

When parsing markdown with multiple emphasis elements, the children arrays are not independent - modifications to one emphasis node's children affect all other emphasis nodes.

### Expected behavior

Each emphasis node should have its own independent children array, and the `type` property should be set to the string `"emphasis"` rather than referencing the node object itself.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
