# Bug Report

### Describe the bug

I'm experiencing an issue where member expressions (like `obj.property`) are not being included in the output bundle when they should be. It seems like properties accessed via member expressions are being incorrectly tree-shaken out even when they're actually used.

### Reproduction

```js
// Input code
const obj = {
  prop: 'value'
};

console.log(obj.prop);
```

After bundling, the member expression access appears to be missing from the output. The property access should be preserved in the bundle but it's getting removed.

### Expected behavior

Member expressions should be properly included in the bundle when they are used in the code. The property access `obj.prop` should remain in the output.

### Additional context

This seems to have started happening recently. Previously, member expressions were being included correctly in the bundle. Now they're being incorrectly optimized away during the tree-shaking process.

---
Repository: /testbed
