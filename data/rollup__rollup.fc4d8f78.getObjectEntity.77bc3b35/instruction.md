# Bug Report

### Describe the bug

I'm experiencing an issue where static class properties and methods are not being handled correctly. When I define static members in a class, they don't seem to be accessible or are being treated as instance methods instead.

### Reproduction

```js
class MyClass {
  static staticMethod() {
    return 'static';
  }
  
  static staticProp = 42;
  
  instanceMethod() {
    return 'instance';
  }
}

// Static members should be accessible on the class itself
console.log(MyClass.staticMethod()); // Expected: 'static'
console.log(MyClass.staticProp); // Expected: 42
```

### Expected behavior

Static properties and methods should be accessible directly on the class constructor, not on instances. The bundler should correctly distinguish between static and instance members.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
