# Bug Report

### Describe the bug

I'm experiencing an issue with labeled break statements in switch cases. When a break statement with a label is used inside a switch case, the code after the labeled block is being incorrectly included in the output bundle, even though it should be unreachable.

### Reproduction

```js
label: {
  switch (condition) {
    case 'a':
      break label;
    case 'b':
      doSomething();
      break;
  }
  
  // This code should be tree-shaken as unreachable
  unreachableCode();
}
```

### Expected behavior

The code after the labeled block should be recognized as unreachable and removed during tree-shaking, since the break statement exits the labeled block entirely. Currently, it appears that `unreachableCode()` is being included in the bundle when it shouldn't be.

### Additional context

This seems to affect scenarios where:
- A labeled break is used within a switch statement
- There's code after the switch but still inside the labeled block

The unlabeled break statements within switch cases seem to work fine, it's specifically the combination of labeled breaks inside switches that's problematic.

---
Repository: /testbed
