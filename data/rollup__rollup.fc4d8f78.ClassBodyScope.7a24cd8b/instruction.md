# Bug Report

### Describe the bug

I'm experiencing an issue with class scope handling where `this` variable resolution seems to be broken in certain contexts. When accessing `this` from within a class body, the scope chain doesn't appear to be set up correctly, leading to unexpected behavior.

### Reproduction

```js
class MyClass {
  constructor() {
    // Accessing 'this' here
    this.value = 42;
  }
  
  method() {
    // 'this' reference seems to resolve incorrectly
    return this.value;
  }
}
```

The problem appears when the class body scope tries to resolve the `this` variable. It seems like the parent scope relationship isn't being established properly before the instance scope is created.

### Expected behavior

The `this` variable should resolve correctly in both the class body and instance scopes. The scope chain should be properly initialized so that `this` references work as expected throughout the class definition.

### Additional context

This might be related to how the scope hierarchy is constructed - specifically the order in which parent scopes are assigned versus when child scopes are created. The instance scope should probably inherit from the class body scope, not from the parent scope directly.

---
Repository: /testbed
