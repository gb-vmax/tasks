# Bug Report

### Describe the bug

I've encountered an issue where side effects in my code are not being detected correctly. Functions that should be identified as having side effects are being treated as pure, and vice versa. This is causing incorrect tree-shaking behavior where code with side effects is being removed during the build process.

### Reproduction

```js
// Code with clear side effects (e.g., console.log, mutations)
const myFunction = () => {
  console.log('This has side effects');
  globalState.value = 42;
};

// During bundling, this code is incorrectly removed
// even though it has side effects
```

The bundler seems to be inverting the logic - treating code with side effects as pure and pure code as having side effects. This results in:
- Code that should be preserved being tree-shaken away
- Code that should be optimized away being kept in the bundle

### Expected behavior

The bundler should correctly identify which code has side effects and preserve it during tree-shaking, while removing truly pure code that isn't used.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
