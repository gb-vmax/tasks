# Bug Report

### Describe the bug

I'm experiencing an issue with yield expressions in generator functions. It seems like the tree-shaking behavior has changed and yield statements are now being incorrectly removed from the output even when they have side effects.

### Reproduction

```js
function* generator() {
  yield sideEffect();
  yield anotherSideEffect();
}

function sideEffect() {
  console.log('This should be called');
  return 42;
}

function anotherSideEffect() {
  console.log('This should also be called');
  return 100;
}

const gen = generator();
gen.next();
gen.next();
```

### Expected behavior

The yield expressions with side-effecting arguments should be preserved in the bundled output. Both `sideEffect()` and `anotherSideEffect()` should be called when iterating through the generator.

### Actual behavior

The yield statements appear to be getting incorrectly optimized away or not properly detected as having side effects. The generator function body seems to be treated as if it has no effects when it clearly does.

This is causing issues in production code where we rely on generators with side effects for async operations and state management.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
