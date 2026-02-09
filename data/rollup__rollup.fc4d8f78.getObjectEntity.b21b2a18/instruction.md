# Bug Report

### Describe the bug

I'm encountering an issue with class static fields not being properly handled during tree-shaking. When I define static fields on a class, they seem to be incorrectly included or excluded from the output bundle.

### Reproduction

```js
class MyClass {
  static config = { value: 42 };
  
  method() {
    return 'test';
  }
}

// Accessing the static field
console.log(MyClass.config);
```

When bundling this code, the static field `config` doesn't appear to be processed correctly. It seems like static fields are being filtered out when they shouldn't be, or the logic for determining what belongs on the class vs the prototype is not working as expected.

### Expected behavior

Static fields should be properly retained on the class constructor and be accessible after bundling. The distinction between static properties (which belong to the class constructor) and instance properties (which belong to the prototype) should be maintained correctly.

### Additional context

This appears to affect classes with:
- Static field declarations
- A mix of static and instance members
- Computed property names on static fields

The issue seems related to how the bundler determines which properties should be treated as static vs instance members.

---
Repository: /testbed
