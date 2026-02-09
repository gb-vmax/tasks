# Bug Report

### Describe the bug

When using `for...in` loops with objects that have side effects in their iteration, the loop is being incorrectly optimized away even when it should be preserved. The bundler appears to be treating certain `for...in` statements as having no effects when they actually do have observable side effects.

### Reproduction

```js
const obj = {
  get a() {
    console.log('side effect');
    return 1;
  }
};

for (const key in obj) {
  // Loop body
}
```

The above code should preserve the `for...in` loop because iterating over `obj` triggers the getter which has a side effect (console.log). However, the loop is being removed from the output bundle.

### Expected behavior

The `for...in` loop should be included in the bundle when the right-hand side expression (the object being iterated) has side effects, even if the loop body itself appears to have no effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
