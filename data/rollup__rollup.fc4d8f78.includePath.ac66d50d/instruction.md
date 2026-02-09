# Bug Report

### Describe the bug

I'm experiencing an issue where variable declarations and their parent nodes are being included incorrectly during tree-shaking. It seems like the logic for traversing up the AST to include parent nodes has changed behavior - nodes are now being processed even when they're already included, which causes an infinite loop or stack overflow in certain cases.

### Reproduction

This happens with code that has nested variable declarations:

```js
function outer() {
  function inner() {
    const x = someImportedValue;
    return x.property;
  }
  return inner();
}
```

When tree-shaking tries to include the path for `x.property`, it traverses up through the parent nodes but gets stuck in a loop because the condition for when to stop including parents appears to be inverted.

### Expected behavior

The tree-shaking process should:
1. Include the variable declaration
2. Walk up the parent chain and include each parent node
3. Stop when reaching an already-included node or the Program node

Instead, it seems to continue processing nodes that are already included, leading to redundant work or infinite loops.

### System Info
- Rollup version: latest
- Node version: 18.x

This might be related to how the `while` loop condition checks `node.included` when deciding whether to continue traversing parent nodes.

---
Repository: /testbed
