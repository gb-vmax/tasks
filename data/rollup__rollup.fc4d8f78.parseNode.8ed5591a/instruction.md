# Bug Report

### Describe the bug

I'm encountering an issue with class method scoping where static methods are being treated as instance methods and vice versa. When I define static methods in a class, they seem to have access to instance scope instead of the static scope, and instance methods appear to have static scope.

### Reproduction

```js
class MyClass {
  static staticProp = 'static';
  instanceProp = 'instance';
  
  static staticMethod() {
    // This should access static scope but seems to access instance scope
    return this.staticProp;
  }
  
  instanceMethod() {
    // This should access instance scope but seems to access static scope
    return this.instanceProp;
  }
}
```

When the code is processed, the scope assignment appears to be inverted - static methods get instance scope and instance methods get static scope.

### Expected behavior

Static methods should have access to static scope (class-level properties and methods), while instance methods should have access to instance scope (instance properties and methods). The scoping should correctly distinguish between static and non-static class members.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
