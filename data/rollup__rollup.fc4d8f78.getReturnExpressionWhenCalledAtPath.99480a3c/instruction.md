# Bug Report

### Describe the bug

I'm experiencing an issue with method return value tracking in nested property access scenarios. When calling methods on objects with deep property paths, the return expressions are being incorrectly evaluated.

### Reproduction

```js
const obj = {
  nested: {
    method: function() {
      return someValue;
    }
  }
};

// Calling method on nested path
obj.nested.method();
```

The issue appears when accessing methods through nested property chains. The return value analysis seems to be too strict and returns `UNKNOWN_RETURN_EXPRESSION` in cases where it should be able to determine the actual return type.

### Expected behavior

Methods should be properly analyzed even when accessed through nested property paths (at least for simple nesting levels). The return expression should be correctly determined based on the method's description rather than defaulting to unknown.

### Additional context

This is affecting tree-shaking and optimization capabilities since the system can't properly track what methods return when they're accessed via property chains. The behavior changed recently and is causing some previously optimized code to no longer be optimized correctly.

---
Repository: /testbed
