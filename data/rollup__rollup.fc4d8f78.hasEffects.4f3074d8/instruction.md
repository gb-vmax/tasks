# Bug Report

### Describe the bug

I'm experiencing an issue where member expressions with side effects are not being properly detected during tree-shaking. Code that should be retained because it has side effects is being incorrectly removed from the bundle.

### Reproduction

```js
const obj = {
  get value() {
    console.log('side effect');
    return 42;
  }
};

// This access has a side effect (getter logs to console)
// but it's being removed from the output
obj.value;
```

After bundling, the getter access is completely removed even though it should be preserved due to the side effect in the getter.

### Expected behavior

Member expressions that have side effects (like getters with side effects, or accessing properties on objects with side effects) should be retained in the bundle. The code should not be tree-shaken away when there are observable effects.

### Additional context

This seems to affect property access patterns where either:
- The object being accessed has side effects
- The property key evaluation has side effects  
- The property access itself triggers side effects (e.g., getters)

The bundler is incorrectly optimizing away these expressions, leading to different runtime behavior between source and bundled code.

---
Repository: /testbed
