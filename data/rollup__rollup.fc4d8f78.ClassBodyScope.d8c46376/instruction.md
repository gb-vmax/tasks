# Bug Report

### Describe the bug

I'm experiencing an issue with class instance scopes where `this` references inside class methods are not being resolved correctly. It seems like the scope chain for instance members is broken.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
  
  method() {
    return this.value; // 'this' is not resolving properly
  }
}

const instance = new MyClass();
console.log(instance.method()); // Expected: 42, but getting incorrect behavior
```

When analyzing the scope chain, the `this` variable in instance methods doesn't seem to be pointing to the correct scope. The class body scope and instance scope hierarchy appears to be misconfigured.

### Expected behavior

The `this` keyword inside class methods should correctly reference the class instance and resolve to the proper scope. Instance methods should have access to instance properties through `this`.

### Additional context

This might be related to how the class body scope is set up and how the instance scope inherits from it. The scope chain seems to be incorrectly structured, causing `this` to not resolve as expected in instance contexts.

---
Repository: /testbed
