# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where function calls are being incorrectly removed from the bundle even though they have side effects. The code executes fine in development but after bundling, certain function calls that should be included are missing from the output.

### Reproduction

```js
// input.js
function sideEffect() {
  console.log('This should appear');
  window.globalState = true;
}

// This call gets removed even though it has side effects
sideEffect();

export const foo = 'bar';
```

When bundling this code, the `sideEffect()` call is being removed from the output bundle, even though it clearly has side effects that should be preserved.

### Expected behavior

Function calls with side effects should be included in the bundle and executed. The call to `sideEffect()` should appear in the bundled output and run when the module is loaded.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
