# Bug Report

### Describe the bug

I'm experiencing an issue with link parsing where the structure of generated link nodes appears to be incorrect. When creating links, the `children` property is being set to `null` instead of an empty array, and the `title` property is being set to an empty string instead of `null`.

### Reproduction

```js
// When parsing markdown with links, the resulting AST has incorrect structure
const ast = parse('[link text](http://example.com)');

// The link node has:
// - children: null (should be an empty array [])
// - title: "" (should be null)

console.log(ast.children[0].children); // null
console.log(ast.children[0].title); // ""
```

### Expected behavior

Link nodes should have:
- `children` property initialized as an empty array `[]`
- `title` property set to `null` when no title is provided

This is causing issues when trying to iterate over or manipulate link children, as the code expects an array but gets `null` instead.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
