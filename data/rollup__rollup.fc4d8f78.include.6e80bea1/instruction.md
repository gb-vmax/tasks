# Bug Report

### Describe the bug

I'm experiencing an issue with code inclusion in block statements. It seems like certain nodes that should be included in the output are being skipped during the tree-shaking process.

### Reproduction

```js
// Example code structure
function test() {
  const x = sideEffect();
  return 42;
}

// After bundling, the sideEffect() call is missing from output
// even though it should be included
```

When I have a block statement with nodes that should be included based on `shouldBeIncluded()`, they're not making it into the final bundle. This appears to happen specifically when:

1. The block contains statements with side effects
2. The statements are not directly marked for inclusion but should be included based on context
3. The block itself is being processed during the inclusion phase

### Expected behavior

All nodes within a block statement that return `true` from `shouldBeIncluded(context)` should be included in the output, regardless of whether they're being included recursively or not.

### Additional context

This seems like a regression - the same code was working correctly in previous versions. The issue manifests as missing side effects or statements in the bundled output, which can break application logic.

---
Repository: /testbed
