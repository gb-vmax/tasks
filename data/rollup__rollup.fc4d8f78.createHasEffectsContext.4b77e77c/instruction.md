# Bug Report

### Describe the bug

I'm experiencing an issue where code that should be included in the bundle is being incorrectly tree-shaken away. It appears that the tree-shaking logic is too aggressive and is removing code that has side effects or is actually used.

### Reproduction

```js
// input.js
function doSomething() {
  console.log('This should be included');
  return 42;
}

const result = doSomething();
export { result };
```

When bundling this code, the function call and its side effects are being removed even though they should be preserved. The bundle ends up missing the console.log statement and potentially other important side effects.

### Expected behavior

Code with side effects should be included in the bundle. The tree-shaking algorithm should correctly identify when code needs to be preserved, especially:
- Function calls that may have side effects
- Code in the top-level scope that executes on module load
- Any statements that could modify external state

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression as the same code was bundled correctly in previous versions. The issue appears to affect any code where the effect analysis determines whether statements should be included.

---
Repository: /testbed
