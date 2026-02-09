# Bug Report

### Describe the bug

I've encountered an issue with switch statements where the first case in a switch block is not being properly included/processed. It seems like the first case is being skipped during some internal traversal or analysis.

### Reproduction

```js
switch (value) {
  case 'first':
    doSomething();
    break;
  case 'second':
    doSomethingElse();
    break;
  default:
    doDefault();
}
```

When the above code is processed, the first case (`case 'first'`) appears to be ignored or not included in the output, while subsequent cases work as expected.

### Expected behavior

All cases in a switch statement should be properly included and processed, including the first case. The bundler should treat all cases equally regardless of their position in the switch block.

### Additional context

This seems to have started happening recently. I noticed that when I have a switch statement with multiple cases, only cases after the first one are being handled correctly. The first case is somehow being excluded from the final bundle or not being marked as included during tree-shaking.

---
Repository: /testbed
