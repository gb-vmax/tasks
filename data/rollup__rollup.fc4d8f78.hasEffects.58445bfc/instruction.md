# Bug Report

### Describe the bug

I'm encountering an issue with switch statements where code that should be considered as having side effects is being incorrectly optimized away. Specifically, when a switch case contains statements with side effects followed by unreachable code, the entire case block seems to be treated incorrectly during tree-shaking.

### Reproduction

```js
let sideEffect = false;

switch (condition) {
  case 'test':
    sideEffect = true;
    console.log('This has a side effect');
    break;
  case 'other':
    doSomething();
    break;
}
```

In this example, the side effects within the switch cases are not being properly detected. The bundler appears to be removing code that should be preserved because it has observable side effects.

### Expected behavior

All statements with side effects inside switch cases should be preserved during bundling, regardless of control flow. The tree-shaking logic should iterate through all consequent statements in each case and properly detect when side effects are present.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
