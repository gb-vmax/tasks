# Bug Report

### Describe the bug

When using labeled statements in code, the label removal is not working correctly. The generated output includes unexpected characters or malformed code when the label should be removed but isn't being used.

### Reproduction

```js
// Input code with an unused label
myLabel: {
  console.log('test');
}

// The output is malformed - extra characters remain where the label should have been removed
```

When a labeled statement's label is not included in the final bundle (tree-shaken), the code removal range appears to be incorrect, leaving behind parts of the original label or colon in the output.

### Expected behavior

When a label is unused and removed during tree-shaking, the entire label declaration including the colon should be cleanly removed, leaving only the statement body. The output should be valid JavaScript without any leftover characters from the removed label.

### Additional context

This seems to affect labeled statements specifically when the label itself is determined to be unused but the body needs to be preserved. The generated code has syntax issues in the final bundle.

---
Repository: /testbed
