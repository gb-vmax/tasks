# Bug Report

### Describe the bug

I'm experiencing an issue where member expressions on objects are being incorrectly tree-shaken even when `propertyReadSideEffects` is set to `'always'`. It seems like property accesses that should be preserved are getting removed during the build process.

### Reproduction

```js
// config
export default {
  treeshake: {
    propertyReadSideEffects: 'always'
  }
}

// code
const obj = getObject();
obj.property; // This access gets removed even though it might have side effects
```

When I build with `propertyReadSideEffects: 'always'`, I expect all property accesses to be preserved in the output, but they're being tree-shaken away. This is causing issues where side effects from getters are not being executed.

### Expected behavior

With `propertyReadSideEffects: 'always'`, all member expression accesses should be preserved in the bundled output, regardless of whether the result is used or not.

### Additional context

This seems to have started happening recently. When I set the option to `'always'`, the property reads should never be removed since they could have side effects (like getters that log, track analytics, etc).

---
Repository: /testbed
