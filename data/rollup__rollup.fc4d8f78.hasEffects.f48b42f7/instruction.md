# Bug Report

### Describe the bug

I've encountered an issue with labeled break statements in switch cases. When a break statement with a label is used inside a switch case, the code is incorrectly being tree-shaken even though it should be included in the output.

### Reproduction

```js
function test(value) {
  outer: switch (value) {
    case 1:
      break outer;
    case 2:
      console.log('case 2');
      break;
  }
  console.log('after switch');
}

test(1);
```

### Expected behavior

The labeled break statement should be preserved in the output and the code should work correctly. The `console.log('after switch')` should execute when `value` is 1.

### Actual behavior

The labeled break statement appears to be removed or not properly tracked during the tree-shaking process, causing incorrect code elimination.

This seems to have started happening recently. Unlabeled break statements work fine, but adding a label causes the issue.

---
Repository: /testbed
