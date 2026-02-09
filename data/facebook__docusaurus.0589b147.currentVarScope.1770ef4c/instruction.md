# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where it seems to be accessing array indices incorrectly when traversing scope stacks. This is causing unexpected behavior when parsing certain MDX files with nested scopes.

### Reproduction

When parsing MDX content with function scopes or block-level declarations, the parser appears to skip the current scope and starts checking from an out-of-bounds index. This leads to either accessing `undefined` or skipping the most recent scope entirely.

```js
// Example MDX that triggers the issue
function example() {
  var x = 1;
  {
    let y = 2;
  }
}
```

The parser seems to be looking at the wrong scope when trying to resolve variable declarations, starting from an index that's one beyond the actual array length.

### Expected behavior

The scope stack traversal should start from the last valid index (length - 1) to properly check the current scope first before moving to parent scopes.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
