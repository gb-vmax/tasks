# Bug Report

### Describe the bug

I'm experiencing an issue where side effects in the initialization part of `for` loops are not being properly detected. When a `for` loop has an initializer that contains side effects (like function calls or assignments), the bundler doesn't seem to recognize these as having effects, which can lead to incorrect tree-shaking behavior.

### Reproduction

```js
let count = 0;

function incrementCount() {
  count++;
  return 0;
}

// The incrementCount() call in the init should be preserved
// because it has side effects, but it's being removed
for (let i = incrementCount(); i < 10; i++) {
  console.log(i);
}

console.log(count); // Expected: 1, but the increment might not happen
```

Another example:

```js
const state = { value: 0 };

for (state.value = 5; state.value < 10; state.value++) {
  // loop body
}

// state.value should be modified by the loop initialization
```

### Expected behavior

The bundler should recognize that the initialization expression in a `for` loop can have side effects and should not be removed during tree-shaking. Any function calls, assignments, or other operations with side effects in the `for` loop's init section should be preserved in the output.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
