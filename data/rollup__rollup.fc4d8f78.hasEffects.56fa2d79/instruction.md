# Bug Report

### Describe the bug

Tree-shaking is incorrectly removing spread elements when `propertyReadSideEffects` is set to a truthy value but not `'always'`. The spread operator should be preserved when property reads can have side effects, but it's being removed in certain configurations.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  },
  treeshake: {
    propertyReadSideEffects: true
  }
}

// src/index.js
const obj = {
  get value() {
    console.log('side effect!');
    return 42;
  }
};

const spread = [...obj];
```

### Expected behavior

When `propertyReadSideEffects` is enabled (set to `true`), the spread operation should be preserved in the output since accessing properties during the spread could trigger getters with side effects. The console.log should execute.

### Actual behavior

The spread element is being tree-shaken out even though property reads can have side effects. The side effect from the getter is lost.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
