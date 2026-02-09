# Bug Report

### Describe the bug

I'm experiencing an issue with temporal dead zone (TDZ) detection in my code. Variables that should be flagged as TDZ violations are not being caught, and conversely, some valid variable accesses are being incorrectly marked as TDZ errors.

### Reproduction

```js
// Case 1: This should throw a TDZ error but doesn't
function test1() {
  console.log(x); // Should error - accessing before declaration
  let x = 5;
}

// Case 2: This throws an error but shouldn't
function test2() {
  let y = 10;
  console.log(y); // Valid access but getting flagged
}
```

### Expected behavior

- Variables accessed before their declaration (within the same scope) should be properly detected as TDZ violations
- Variables accessed after their declaration should work normally without false TDZ errors

### System Info
- Rollup version: latest
- Node version: 18.x

The TDZ checking logic seems to be inverted somehow - it's catching the wrong cases. This is causing both false positives and false negatives in my builds.

---
Repository: /testbed
