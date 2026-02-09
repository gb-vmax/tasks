# Bug Report

### Describe the bug

Tagged template expressions with side effects in the tag function are not being properly detected, causing side-effectful code to be incorrectly removed during tree-shaking.

### Reproduction

```js
let sideEffect = false;

function tagWithSideEffect(strings, ...values) {
  sideEffect = true;
  return strings[0];
}

// This tagged template should be preserved because the tag function has side effects
tagWithSideEffect`hello ${world}`;

// The side effect is not triggered after bundling
console.log(sideEffect); // Expected: true, Actual: false (code was removed)
```

### Expected behavior

When a tagged template expression's tag function has side effects (like modifying external state), the entire expression should be preserved during tree-shaking and not removed as dead code. The `hasEffects` check should properly account for side effects from the tag function's interaction.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
