# Bug Report

### Describe the bug
I'm encountering an issue with the remark parser where it seems to be creating malformed fragment nodes. When parsing markdown content, the resulting AST contains unexpected structure in fragment nodes.

### Reproduction
```js
const remark = require('remark');

const markdown = `
# Test

Some content here
`;

const result = remark().parse(markdown);
// Fragment nodes in the AST have incorrect structure
// Expected: { type: "fragment", children: [] }
// Actual: { type: "fragments", children: [{}] }
```

### Expected behavior
Fragment nodes should have:
- `type` property set to `"fragment"` (singular)
- `children` property initialized as an empty array `[]`

Instead, they're being created with:
- `type` property set to `"fragments"` (plural)
- `children` property containing an empty object `[{}]`

This breaks downstream processing that expects the standard fragment node structure.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
