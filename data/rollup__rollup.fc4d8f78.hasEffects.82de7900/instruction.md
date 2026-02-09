# Bug Report

### Describe the bug

I'm experiencing an issue where side effects from member expressions are not being properly detected during tree-shaking. The bundler is incorrectly removing code that should be kept because it has side effects.

### Reproduction

```js
const obj = {
  get value() {
    console.log('side effect!');
    return 42;
  }
};

// This should be kept because accessing the getter has side effects
obj.value;

// After bundling, this code is removed even though it should be kept
```

Another example:

```js
const state = {};
Object.defineProperty(state, 'prop', {
  get() {
    // Side effect that should be preserved
    window.globalCounter++;
    return 'value';
  }
});

// This access has side effects but gets tree-shaken out
state.prop;
```

### Expected behavior

Member expressions that have side effects (like getter functions with side effects, or property access on objects with Proxy handlers) should be preserved during tree-shaking and not removed from the final bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression - the previous version was correctly keeping these expressions in the bundle.

---
Repository: /testbed
