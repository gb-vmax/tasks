# Bug Report

### Describe the bug

I'm encountering an issue with `super` keyword handling in class methods. When using `super` to call parent class methods or access parent properties, the behavior seems incorrect and the code doesn't work as expected.

### Reproduction

```js
class Parent {
  method() {
    return 'parent';
  }
}

class Child extends Parent {
  method() {
    return super.method(); // This doesn't work correctly
  }
}

const instance = new Child();
console.log(instance.method()); // Expected: 'parent', but behavior is broken
```

### Expected behavior

The `super` keyword should correctly resolve to the parent class and allow calling parent methods or accessing parent properties. The child class method should be able to invoke the parent's implementation using `super.method()`.

### Additional context

This seems to affect any usage of `super` in class hierarchies. The issue appears in both method calls and property access through `super`.

---
Repository: /testbed
