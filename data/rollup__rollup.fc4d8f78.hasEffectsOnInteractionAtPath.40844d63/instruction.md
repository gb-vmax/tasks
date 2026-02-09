# Bug Report

### Describe the bug

Functions marked with `@__NO_SIDE_EFFECTS__` annotation are being treated incorrectly when accessing nested properties or methods. The side effect detection seems to be inverted - it's returning `false` (no side effects) for property access paths instead of direct function calls.

### Reproduction

```js
// Function with no side effects annotation
/*#__NO_SIDE_EFFECTS__*/
function createObject() {
  return {
    method() {
      console.log('side effect');
    }
  };
}

// Calling the annotated function directly should be treated as having no side effects
const obj = createObject();

// But accessing properties/methods on the result should still be analyzed for side effects
obj.method(); // This should be checked for side effects but isn't
```

### Expected behavior

When a function is annotated with `@__NO_SIDE_EFFECTS__`, only the direct call to that function (path length === 0) should be considered side-effect-free. Any property access or method calls on the returned value (path length > 0) should still be properly analyzed for side effects.

Currently it seems like the logic is backwards - property accesses are being marked as side-effect-free when they shouldn't be.

### System Info

- rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed
