# Bug Report

### Describe the bug

Arrow functions are being incorrectly marked as having side effects, causing them to be retained in the bundle even when they're never called or used. This leads to unnecessary code bloating in the output.

### Reproduction

```js
// This unused arrow function gets included in the bundle
const unusedFn = () => {
  console.log('This should be tree-shaken');
};

// Only this should be in the final output
export const used = 42;
```

When bundling the above code, the `unusedFn` arrow function appears in the output even though it's never referenced or called anywhere. It should be removed during tree-shaking since it has no side effects.

### Expected behavior

Unused arrow functions that don't have side effects should be tree-shaken and removed from the final bundle. Only the exported `used` constant should remain in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
