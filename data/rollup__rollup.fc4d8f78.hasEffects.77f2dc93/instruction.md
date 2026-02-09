# Bug Report

### Describe the bug

I'm encountering an issue with switch statement tree-shaking where cases with side effects in their test expressions are being incorrectly removed during the build process. The bundler seems to be treating these cases as if they have no effects, even when the test condition contains function calls or other operations that should be preserved.

### Reproduction

```js
let sideEffect = 0;

function incrementAndReturn(val) {
  sideEffect++;
  return val;
}

switch (value) {
  case incrementAndReturn(1):
    console.log('case 1');
    break;
  case incrementAndReturn(2):
    console.log('case 2');
    break;
  default:
    console.log('default');
}

// Expected: sideEffect should be incremented even if cases don't match
// Actual: side effects from test expressions are not being preserved
```

Additionally, switch cases that should execute their consequent statements are being skipped entirely. It seems like the flow control logic for determining which statements to include might be inverted.

### Expected behavior

1. Test expressions in switch cases should always be evaluated for side effects, regardless of whether the case matches
2. Consequent statements in matching cases should be included in the output bundle
3. The bundler should correctly track control flow through switch statements

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
