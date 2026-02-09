# Bug Report

### Describe the bug

When using `super` in class methods, the variable resolution is incorrectly pointing to the wrong scope variable. This causes issues when trying to call parent class methods or access parent class properties through `super`.

### Reproduction

```js
class Parent {
  method() {
    return 'parent';
  }
}

class Child extends Parent {
  method() {
    return super.method(); // This doesn't resolve correctly
  }
}

const instance = new Child();
console.log(instance.method()); // Expected: 'parent', but super reference is broken
```

### Expected behavior

The `super` keyword should correctly resolve to the parent class context and allow calling parent methods/accessing parent properties. Currently it seems to be resolving to the wrong variable in the scope chain.

### Additional context

This appears to affect any usage of `super` in class methods, including:
- `super.method()` calls
- `super.property` access
- Constructor `super()` calls

The issue is causing the bundler to incorrectly handle class inheritance patterns.

---
Repository: /testbed
