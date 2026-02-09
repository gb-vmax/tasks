# Bug Report

### Describe the bug

I'm experiencing an issue with generator functions where yield expressions aren't being properly tree-shaken when they should be. It seems like side effects from yield expressions are not being tracked correctly, causing code that should be removed during optimization to remain in the bundle.

### Reproduction

```js
function* myGenerator() {
  const value = someComputation();
  yield value;
  // More code here that should potentially be tree-shaken
}

// When this generator is not actually used in a way that consumes the yielded values,
// the yield expression and related code should be optimized away
```

The yield expression appears to be treated as having side effects even in contexts where it shouldn't, preventing proper dead code elimination.

### Expected behavior

Yield expressions should be properly analyzed for side effects and tree-shaken when appropriate. If the generator function's yielded values are never consumed or the generator itself is not used, the bundler should be able to optimize away the unnecessary code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
