# Bug Report

### Describe the bug

Tagged template expressions with side effects in their template arguments are being incorrectly tree-shaken/removed during the build process. When a tagged template literal contains expressions that have side effects (like function calls, assignments, etc.), these side effects are not being preserved in the output bundle.

### Reproduction

```js
let counter = 0;

function increment() {
  counter++;
  return counter;
}

// Tagged template with side effect in expression
myTag`Value: ${increment()}`;

console.log(counter); // Expected: 1, but the increment() call gets removed
```

Another example:

```js
const results = [];

function track(value) {
  results.push(value);
  return value;
}

customTag`Processing ${track('item1')} and ${track('item2')}`;

// results array should contain ['item1', 'item2'] but it's empty
```

### Expected behavior

Template expressions that contain side effects should be evaluated and their side effects should be preserved in the bundled output, even if the result of the tagged template expression itself is unused.

### Additional context

This appears to affect any tagged template literal where the template arguments have side effects. The side effects are being incorrectly optimized away during the tree-shaking phase.

---
Repository: /testbed
