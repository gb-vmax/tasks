# Bug Report

### Describe the bug
When using `super` in class methods, the reference is not being resolved correctly. The `super` keyword appears to be broken and doesn't properly bind to the parent class context.

### Reproduction
```js
class Parent {
  method() {
    return 'parent';
  }
}

class Child extends Parent {
  method() {
    return super.method(); // This doesn't work as expected
  }
}

const instance = new Child();
instance.method(); // Fails to execute correctly
```

### Expected behavior
The `super` keyword should correctly reference the parent class and allow calling parent methods. The code above should return 'parent' when calling `instance.method()`.

### Additional context
This seems to affect any code using `super` in class hierarchies. The binding mechanism for `super` appears to be malfunctioning.

---
Repository: /testbed
