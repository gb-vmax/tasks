# Bug Report

### Describe the bug

I'm experiencing an issue with labeled break statements in switch cases. When using a labeled break inside a switch statement, the control flow doesn't exit the labeled block properly - it seems to be breaking out of the switch instead of the labeled statement.

### Reproduction

```js
label: {
  switch (value) {
    case 1:
      break label;
    case 2:
      doSomething();
  }
  // This code should be skipped when break label is hit
  afterSwitch();
}
```

In the above code, when `value` is 1, the `break label` should exit the entire labeled block, skipping `afterSwitch()`. However, the current behavior seems incorrect - the code after the switch statement is still being executed.

### Expected behavior

When a labeled break statement is used inside a switch case, it should break out of the labeled block, not just the switch statement. The control flow should skip any code between the switch and the end of the labeled block.

### Additional context

This appears to affect how the bundler handles control flow analysis for labeled break statements. The issue manifests when trying to tree-shake code that comes after a switch statement within a labeled block.

---
Repository: /testbed
