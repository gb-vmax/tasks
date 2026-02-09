# Bug Report

### Describe the bug

I'm experiencing an issue where `for` loops with side effects in their initialization, test, or update expressions are being incorrectly tree-shaken from the bundle. The code inside these expressions should be preserved when they have side effects, but they're being removed during optimization.

### Reproduction

```js
let counter = 0;

// This for loop should be included in the output because the init has side effects
for (counter++; counter < 5; counter++) {
  // empty body
}

console.log(counter); // Should print 5, but the for loop gets removed
```

Another example:

```js
const arr = [];

// The update expression has side effects that should be preserved
for (let i = 0; i < 3; arr.push(i++)) {
  // empty body
}

console.log(arr); // Expected: [0, 1, 2], but the loop is tree-shaken
```

### Expected behavior

For loops should be retained in the bundle when their init, test, or update expressions contain side effects, even if the loop body is empty. The side effects in these expressions should not be removed during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
