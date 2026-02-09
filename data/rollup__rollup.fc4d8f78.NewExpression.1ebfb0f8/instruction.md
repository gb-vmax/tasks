# Bug Report

### Describe the bug

I'm experiencing an issue with `#__PURE__` annotations on `new` expressions. When a constructor is annotated with `#__PURE__`, the side effects of evaluating the callee expression itself are being ignored during tree-shaking.

### Reproduction

```js
// input.js
const obj = {
  get Constructor() {
    console.log('side effect');
    return class {};
  }
};

// This should preserve the getter side effect even with #__PURE__
const instance = /*#__PURE__*/ new obj.Constructor();
```

When bundling this code, the side effect from the getter (`console.log('side effect')`) is incorrectly being removed, even though accessing `obj.Constructor` has observable effects.

### Expected behavior

The `#__PURE__` annotation should only indicate that the constructor call itself is pure, but side effects from evaluating the callee expression (like property access with getters) should still be preserved.

Currently, it seems like the annotation is causing the entire expression evaluation to be treated as side-effect-free, which is incorrect.

### Additional context

This appears to affect tree-shaking optimization where code that should be retained is being incorrectly removed from the bundle.

---
Repository: /testbed
