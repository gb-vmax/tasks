# Bug Report

### Describe the bug
When processing literal nodes in the AST generator, nodes with `undefined` raw values are being written as `undefined` instead of falling through to the proper stringify logic. This causes incorrect code generation for certain literal types.

### Reproduction
```js
// Create a literal node without a raw property
const literalNode = {
  type: 'Literal',
  value: 'some string',
  // raw is undefined
}

// The generator writes 'undefined' instead of '"some string"'
```

### Expected behavior
When a literal node doesn't have a `raw` property (i.e., `raw` is `undefined`), the generator should fall through to use `stringify(node.value)` to properly format the literal value. The output should be the correctly stringified representation of the value, not the string "undefined".

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: Latest

This seems to have been introduced in a recent change to the Literal handling logic. The condition check appears to be inverted or incorrect.

---
Repository: /testbed
