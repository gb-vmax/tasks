# Bug Report

### Describe the bug

I'm encountering an issue with class bodies where the order of processing appears to be reversed. When working with classes that have multiple methods or properties, they seem to be getting included in the wrong order, which is causing unexpected behavior in my bundled output.

Additionally, there seems to be a problem with how static vs instance members are being scoped. Static class members are being treated as instance members and vice versa, which is breaking the expected behavior of class definitions.

### Reproduction

```js
class MyClass {
  static staticMethod() {
    console.log('static');
  }
  
  instanceMethod() {
    console.log('instance');
  }
  
  anotherMethod() {
    console.log('another');
  }
}
```

When bundling code with classes like the above, the methods appear to be processed in reverse order, and static methods are incorrectly scoped as instance methods (and instance methods as static).

### Expected behavior

- Class body members should be processed in the order they are defined
- Static methods should be correctly identified and scoped as static
- Instance methods should be correctly identified and scoped as instance members

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues in production builds where the order of class member initialization matters, and where static vs instance method distinction is critical.

---
Repository: /testbed
