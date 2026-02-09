# Bug Report

### Describe the bug

I'm experiencing an issue with class declarations where the identifier scope is not being resolved correctly. When working with named classes, the class name identifier seems to be getting the wrong scope context.

### Reproduction

```js
class MyClass {
  constructor() {
    // Class body
  }
}

// The class identifier 'MyClass' is not being resolved with the correct scope
// This affects how the class name is accessible within its own body
```

### Expected behavior

The class identifier should use the parent scope for proper resolution. The class name should be accessible and resolve correctly in contexts where it references itself.

### Additional context

This appears to affect named class declarations specifically. The scope being passed to the Identifier constructor seems incorrect, which could lead to issues with class name resolution and self-referencing scenarios.

---
Repository: /testbed
