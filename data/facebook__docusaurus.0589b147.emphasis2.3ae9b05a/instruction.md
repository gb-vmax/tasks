# Bug Report

### Describe the bug

I'm experiencing issues with emphasis nodes in markdown processing. When parsing markdown with emphasized text (using `*` or `_`), the resulting AST structure appears to be malformed. The emphasis node's type property is returned as an array instead of a string, and the children property is null instead of an empty array.

### Reproduction

```js
import {remark} from 'remark';

const markdown = '*emphasized text*';
const tree = remark.parse(markdown);

// The emphasis node has incorrect structure
console.log(tree.children[0].children[0]);
// Expected: { type: 'emphasis', children: [...] }
// Actual: { type: ['emphasis'], children: null }
```

When trying to traverse or manipulate the AST, this causes errors because:
1. The `type` property is an array `['emphasis']` instead of the string `'emphasis'`
2. The `children` property is `null` instead of an empty array `[]`

This breaks any code that expects the standard mdast format where type is always a string and children is always an array.

### Expected behavior

Emphasis nodes should follow the standard mdast node structure:
- `type` should be a string value `"emphasis"`
- `children` should be an array (empty or containing child nodes)

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
