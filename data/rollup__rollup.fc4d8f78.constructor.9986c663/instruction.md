# Bug Report

### Describe the bug

I'm experiencing an issue with class scope handling where the `this` variable in instance methods doesn't resolve correctly to the class instance scope. Instead, it seems to be pointing to the wrong scope level, causing unexpected behavior when accessing instance properties or methods through `this`.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
  
  method() {
    // this.value should reference the instance property
    // but it's not resolving correctly
    return this.value;
  }
}

const instance = new MyClass();
instance.method(); // Expected to work but fails to resolve 'this' properly
```

### Expected behavior

The `this` keyword inside instance methods should correctly reference the instance scope where instance properties are accessible. The instance scope should be properly linked to the class body scope hierarchy.

### Additional context

This appears to be related to how the instance scope is being initialized - it seems like the parent scope relationship might not be set up correctly, causing the scope chain to break when trying to resolve `this` in instance contexts.

---
Repository: /testbed
