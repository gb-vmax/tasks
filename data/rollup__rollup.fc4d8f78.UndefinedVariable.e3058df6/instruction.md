# Bug Report

### Describe the bug

I'm experiencing an issue where `undefined` values are being transformed incorrectly in the output. When my code uses `undefined`, the bundler is replacing it with `void 0` in the generated output, but the actual runtime value is coming back as `null` instead of `undefined`.

### Reproduction

```js
// Input code
const myVar = undefined;
console.log(myVar === undefined); // Should be true
console.log(typeof myVar); // Should be 'undefined'

// After bundling, the behavior changes
// The value is null instead of undefined
```

This seems to affect any code that checks for `undefined` values or relies on the distinction between `null` and `undefined`.

### Expected behavior

When the code uses `undefined`, the bundled output should preserve the correct `undefined` semantics. The value should remain `undefined` at runtime, not become `null`.

### Additional context

This appears to have started happening recently. My code that previously worked correctly now fails when checking for `undefined` values. The transformation to `void 0` is fine (that's a standard optimization), but the actual value being `null` breaks the expected behavior.

---
Repository: /testbed
