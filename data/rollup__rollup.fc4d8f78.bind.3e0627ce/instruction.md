# Bug Report

### Describe the bug

When using `super` keyword in class methods, the code is not working correctly. It seems like the variable binding for `super` is broken - instead of properly resolving the `super` reference, it's trying to find a variable named 'super' in the scope which doesn't make sense.

### Reproduction

```js
class Parent {
  method() {
    return 'parent';
  }
}

class Child extends Parent {
  method() {
    return super.method(); // This fails
  }
}

const instance = new Child();
console.log(instance.method()); // Expected: 'parent', but super is not resolved correctly
```

### Expected behavior

The `super` keyword should properly reference the parent class methods and properties. The code should execute without errors and `super.method()` should call the parent's method.

### Additional context

This appears to be related to how the AST handles the `super` node during the binding phase. The variable resolution seems incorrect.

---
Repository: /testbed
