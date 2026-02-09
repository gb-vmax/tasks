# Bug Report

### Describe the bug

I'm encountering an issue with class definitions where static and instance members are being assigned to the wrong scopes. It seems like static methods/properties are being treated as instance members and vice versa.

### Reproduction

```js
class MyClass {
  static staticMethod() {
    return this.staticProp;
  }
  
  static staticProp = 'static';
  
  instanceMethod() {
    return this.instanceProp;
  }
  
  instanceProp = 'instance';
}

// Static members behave like instance members
// Instance members behave like static members
```

When bundling code with class definitions, the scope resolution appears to be reversed - static class members are being resolved in the instance scope and instance members in the static scope.

### Expected behavior

Static methods and properties should be resolved in the class's static scope, while instance methods and properties should be resolved in the instance scope.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
