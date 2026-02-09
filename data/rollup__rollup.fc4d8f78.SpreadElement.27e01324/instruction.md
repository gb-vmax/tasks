# Bug Report

### Describe the bug

I'm experiencing an issue with spread operators in object/array literals where they're not being handled correctly during tree-shaking. The bundler seems to be incorrectly evaluating side effects and deoptimization paths for spread elements.

### Reproduction

```js
// Case 1: Spread with side effects
const obj = {
  get value() {
    console.log('side effect');
    return 42;
  }
};

const result = [...someArray, ...obj];
```

```js
// Case 2: Nested spread operations
const nested = {
  ...{
    ...deepObject
  }
};
```

In both cases, the spread operation doesn't seem to be properly analyzing whether the argument has side effects or when to deoptimize paths. The bundler output is either incorrectly including or excluding code that should/shouldn't be tree-shaken.

### Expected behavior

- Spread elements should correctly detect side effects in their arguments
- Property reads with side effects should be preserved when `propertyReadSideEffects` is enabled
- Deoptimization should only occur when necessary (e.g., when path length conditions are met)

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
