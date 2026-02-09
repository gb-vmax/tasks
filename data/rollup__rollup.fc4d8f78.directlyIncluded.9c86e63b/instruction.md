# Bug Report

### Describe the bug

I'm experiencing an issue where code inside block statements is being included in the bundle even when it should be tree-shaken away. It seems like the logic for determining whether a block is directly included might be inverted.

### Reproduction

```js
// Example code that should be tree-shaken
if (false) {
  console.log('This should never be included');
  someUnusedFunction();
}

// Or with unused functions
function unusedHelper() {
  {
    console.log('Nested block that should be removed');
  }
}
```

When bundling this code, the content inside these blocks is being included in the output even though they're unreachable or unused.

### Expected behavior

Dead code inside block statements should be properly tree-shaken and excluded from the final bundle. Unreachable blocks and unused function bodies should not appear in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
