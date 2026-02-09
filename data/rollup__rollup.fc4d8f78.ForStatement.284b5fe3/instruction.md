# Bug Report

### Describe the bug

I'm experiencing an issue with `for` loops where side effects in the loop's init, test, or update expressions are not being detected correctly. This causes the bundler to incorrectly remove code that should be kept because it has side effects.

### Reproduction

```js
let counter = 0;

for (let i = 0; i < 10; sideEffect()) {
  // loop body
}

function sideEffect() {
  counter++;
}

console.log(counter); // Expected: 10, but code gets removed
```

Another example where the init expression has side effects:

```js
let initialized = false;

for (init(); i < 10; i++) {
  // loop body
}

function init() {
  initialized = true;
  return (i = 0);
}

// The init() call gets removed even though it has side effects
```

### Expected behavior

The bundler should preserve `for` loops when any of the three expressions (init, test, or update) contain side effects. Currently it seems like code with side effects in these expressions is being incorrectly tree-shaken.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed
