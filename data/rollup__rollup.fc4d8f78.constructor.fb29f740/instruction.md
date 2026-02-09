# Bug Report

### Describe the bug

I'm encountering an issue with `this` variable resolution in class bodies. It seems like the `this` variable is being set incorrectly in the instance scope, causing unexpected behavior when accessing `this` within class methods.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
  
  method() {
    return this.value;
  }
}
```

When the class is processed, the `this` variable in the instance scope appears to be referencing the wrong variable. Instead of pointing to the `ThisVariable`, it's being overwritten with a `LocalVariable`.

### Expected behavior

The `this` variable in the instance scope should properly resolve to a `ThisVariable` instance, not a `LocalVariable`. Class methods should be able to correctly access instance properties through `this`.

### Additional context

This might be related to how the class body scope and instance scope are being initialized. The order of operations when setting up these scopes seems important here.

---
Repository: /testbed
