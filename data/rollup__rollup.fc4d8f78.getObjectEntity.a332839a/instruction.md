# Bug Report

### Describe the bug

I'm encountering an issue with class field tree-shaking. It seems like static class fields are not being properly handled, causing them to be incorrectly included or excluded during the tree-shaking process.

### Reproduction

```js
class MyClass {
  static staticField = 'value';
  instanceField = 'instance';
  
  static staticMethod() {
    return 'static';
  }
  
  instanceMethod() {
    return 'instance';
  }
}

// When bundling, static fields seem to be treated incorrectly
export { MyClass };
```

The bundler appears to be processing static fields differently than expected. Static properties should remain on the class constructor, but they seem to be getting mixed up with instance properties.

### Expected behavior

Static class fields should be properly distinguished from instance fields during tree-shaking. The class structure should be preserved correctly with:
- Static fields on the class constructor itself
- Instance fields on class instances (not on the prototype)
- Methods on the appropriate location (static methods on constructor, instance methods on prototype)

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
