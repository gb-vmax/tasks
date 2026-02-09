# Bug Report

### Describe the bug

Arrow functions annotated with `@__NO_SIDE_EFFECTS__` are not being properly recognized when called directly. The tree-shaking optimization appears to be incorrectly evaluating whether these functions have side effects, causing them to be retained in the bundle even when their return values are unused.

### Reproduction

```js
/* @__NO_SIDE_EFFECTS__ */
const pureFunction = () => {
  return { data: 'test' };
};

// This call should be tree-shaken since the result is unused
pureFunction();

// Expected: function call removed in production build
// Actual: function call retained in bundle
```

Also seeing issues with IIFE (Immediately Invoked Function Expressions) detection for arrow functions. Arrow functions that are NOT immediately invoked are being incorrectly treated as IIFEs, which affects how they're processed during bundling.

```js
const myArrowFn = () => console.log('hello');
const result = someFunction(myArrowFn);

// The arrow function is being incorrectly identified as an IIFE
// causing unexpected bundling behavior
```

### Expected behavior

- Arrow functions marked with `@__NO_SIDE_EFFECTS__` should be properly tree-shaken when their results are unused
- IIFE detection should correctly identify only arrow functions that are actually immediately invoked
- Non-IIFE arrow functions should be handled appropriately during bundling

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
