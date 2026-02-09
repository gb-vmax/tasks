# Bug Report

### Describe the bug

I'm encountering an issue with unlabeled `break` statements in switch cases. When a switch case contains only a `break` statement without a label, the break statement is not being included in the output bundle, causing the code to fall through to the next case unexpectedly.

### Reproduction

```js
function test(value) {
  switch (value) {
    case 1:
      console.log('one');
      break;
    case 2:
      console.log('two');
      break;
    default:
      console.log('default');
  }
}

test(1);
```

### Expected behavior

The function should log `'one'` and then exit the switch statement. Instead, it appears the unlabeled `break` statement is being excluded from the bundle, causing execution to fall through to subsequent cases.

This seems to happen specifically when the `break` statement doesn't have a label. Labeled break statements appear to work correctly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
