# Bug Report

### Describe the bug

When using spread operators with objects that have getters with side effects, the tree-shaking behavior is incorrect. The code is being removed even when `propertyReadSideEffects` is set to `true`, causing side effects to be lost during bundling.

### Reproduction

```js
// input.js
const obj = {
  get value() {
    console.log('side effect!');
    return 42;
  }
};

const spread = { ...obj };
```

With the following rollup config:
```js
{
  treeshake: {
    propertyReadSideEffects: true
  }
}
```

### Expected behavior

The spread operation should be preserved in the output since accessing the getter has side effects and `propertyReadSideEffects` is enabled. The console.log should execute.

### Actual behavior

The spread operation gets tree-shaken away and the side effect is lost. The getter is never invoked.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
