# Bug Report

### Describe the bug

When generating code from MDX/JSX AST nodes with block statements containing multiple statements, the first statement in the block is being skipped and not included in the output. This causes the generated code to be incomplete and potentially break functionality.

### Reproduction

```js
// Given an AST with a BlockStatement containing multiple statements:
const ast = {
  type: 'BlockStatement',
  body: [
    { type: 'ExpressionStatement', ... },  // This gets skipped
    { type: 'ExpressionStatement', ... },
    { type: 'ReturnStatement', ... }
  ]
}

// When generating code from this AST
const output = generate(ast)

// The first statement is missing from the output
// Expected: All three statements in the block
// Actual: Only the last two statements appear
```

### Expected behavior

All statements within a block should be included in the generated output. If a block has three statements, all three should appear in the final code, not just statements 2 and 3.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing issues when transpiling MDX files where the first statement in function bodies or other block contexts gets dropped from the output.

---
Repository: /testbed
