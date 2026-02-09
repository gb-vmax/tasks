# Bug Report

### Describe the bug

I'm experiencing an issue with class field tree-shaking where static class fields are being incorrectly removed from the bundle. The fields are present in the source code but don't appear in the output.

### Reproduction

```js
class MyClass {
  static config = { enabled: true };
  
  static initialize() {
    return this.config;
  }
}

export default MyClass;
```

When bundling this code, the `static config` field gets tree-shaken out even though it's referenced by the `initialize` method. The bundled output only includes the method but not the field, causing runtime errors when `this.config` is accessed.

### Expected behavior

Static class fields should be preserved in the bundle when they are part of the exported class, especially when they're referenced by other static methods. The field should appear in the final output alongside the class definition.

### Additional context

This seems to have started happening recently. Non-static class fields and regular methods work fine, but static fields specifically are being dropped incorrectly.

---
Repository: /testbed
