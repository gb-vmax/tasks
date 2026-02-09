# Bug Report

### Describe the bug

I'm encountering an issue with generator functions that use `yield` expressions. When a generator yields a value without an argument (bare `yield`), the bundler is incorrectly treating it as having side effects and including code that should be tree-shaken away.

### Reproduction

```js
function* myGenerator() {
  yield; // bare yield without argument
  console.log('This should be tree-shaken');
}

// When this generator is not actually called anywhere,
// the console.log still appears in the bundle
```

The problem seems to be that yield expressions without arguments are not being properly analyzed for side effects. This causes dead code to remain in the final bundle even though it's never executed.

### Expected behavior

When a generator function is unused and contains only `yield` statements without arguments, the entire function body should be tree-shaken from the bundle since it has no observable side effects.

### Additional context

This appears to affect any generator that uses bare `yield` statements. Generators with `yield someValue` seem to work correctly, but `yield` by itself is causing issues with the tree-shaking optimization.

---
Repository: /testbed
