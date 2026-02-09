# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where code inside switch statements is being incorrectly removed even when it has side effects. Specifically, when a switch statement doesn't have a default case, code that should be retained is being eliminated from the bundle.

### Reproduction

```js
function test(value) {
  switch (value) {
    case 'a':
      console.log('case a');
      break;
    case 'b':
      console.log('case b');
      break;
  }
  // Code after switch without default case
  sideEffect();
}
```

When bundling this code, the `sideEffect()` call is being removed from the output even though it should always execute (since there's no default case that would cause a broken flow).

### Expected behavior

Code following a switch statement without a default case should be preserved in the bundle, as execution will continue after the switch block regardless of which case matches. The tree-shaking algorithm should recognize that the control flow is not broken when there's no default case.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
