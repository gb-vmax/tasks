# Bug Report

### Describe the bug

Switch statements with default cases are not being tree-shaken correctly when the default case appears before the last case. Code that should be removed as dead code is being included in the bundle.

### Reproduction

```js
// input.js
function test(value) {
  switch (value) {
    default:
      console.log('default');
      break;
    case 1:
      console.log('one');
      break;
    case 2:
      console.log('two');
      break;
  }
}

// The default case is not the last case
// Expected: All cases should be properly analyzed for side effects
// Actual: Cases after the default are not being processed correctly
```

When bundling code with a switch statement where the default case is positioned before other cases (not at the end), the tree-shaking analysis doesn't work as expected. This causes the bundler to either include unnecessary code or incorrectly remove code that has side effects.

### Expected behavior

Switch statements should be analyzed correctly regardless of where the default case is positioned. All cases should be properly evaluated for side effects and included/excluded from the bundle accordingly.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
