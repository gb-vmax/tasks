# Bug Report

### Describe the bug

When using `for...in` loops in my code, I'm noticing that some loops are being incorrectly removed during the tree-shaking/bundling process even though they have side effects. The loop body executes code that should prevent the loop from being eliminated, but the bundler is still removing it.

### Reproduction

```js
const obj = { a: 1, b: 2, c: 3 };

for (const key in obj) {
  console.log(key); // This should have side effects
}

// The entire loop gets removed from the bundle even though
// console.log has side effects and should be preserved
```

Another example:

```js
for (const prop in someObject) {
  doSomethingWithSideEffects(prop);
}

// Loop is eliminated despite the function call having side effects
```

### Expected behavior

`for...in` loops should be preserved in the output bundle when:
- The loop body contains statements with side effects (like `console.log`, function calls, etc.)
- The left-hand side (loop variable assignment) has side effects
- The right-hand side (object being iterated) has side effects

The bundler should correctly detect these side effects and not remove the loop.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression in the side effect detection logic for `for...in` statements. The loops are being treated as pure/effect-free when they actually contain impure operations.

---
Repository: /testbed
