# Bug Report

### Describe the bug

I'm encountering an issue with paragraph node creation in the remark compiler. When creating paragraph nodes, the structure appears to be malformed - the `type` property is being set as an object instead of a string, and the `children` property is coming back as `undefined` instead of an empty array.

### Reproduction

```js
// When the compiler creates a paragraph node
const node = paragraph2();

// Expected structure:
// {
//   type: "paragraph",
//   children: []
// }

// Actual structure:
// {
//   type: { value: "paragraph" },
//   children: undefined
// }
```

This is causing downstream issues when trying to traverse or manipulate the AST, since code expects `children` to be an array and `type` to be a string value.

### Expected behavior

The `paragraph2()` function should return a properly structured node with:
- `type` as a string with value `"paragraph"`
- `children` as an empty array `[]`

This would be consistent with other node creation functions like `root2()` and `strong2()` in the same file.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
