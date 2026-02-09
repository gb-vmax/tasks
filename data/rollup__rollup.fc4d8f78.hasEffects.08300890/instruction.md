# Bug Report

### Describe the bug

I'm experiencing an issue where labeled statements with side effects are being incorrectly tree-shaken from my bundle. Code that should be included in the output is being removed, causing runtime errors.

### Reproduction

```js
label: {
  console.log('This should be included');
  break label;
}
```

After bundling, the entire labeled statement block gets removed from the output even though it contains side effects (the console.log). This causes the expected console output to never appear.

### Expected behavior

Labeled statements containing code with side effects should be preserved in the bundle. The console.log statement should execute and produce output.

### Additional context

This seems to affect any labeled statement where the body has side effects. The tree-shaking logic appears to be inverting the detection somehow - statements that should be kept are being removed, and vice versa.

---
Repository: /testbed
