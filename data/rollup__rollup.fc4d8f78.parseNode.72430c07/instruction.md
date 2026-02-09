# Bug Report

### Describe the bug

I'm encountering an issue with class declarations where the scope chain seems to be broken. When I have a named class declaration, the identifier appears to be registered in the wrong scope, causing problems with variable resolution in nested contexts.

### Reproduction

```js
class MyClass {
  constructor() {
    // Reference to MyClass here doesn't resolve correctly
    const ref = MyClass;
  }
}

// Or with class expressions:
const cls = class NamedClass {
  method() {
    // NamedClass reference has scope issues
    return NamedClass;
  }
};
```

### Expected behavior

The class identifier should be properly scoped so that references to the class name within the class body resolve correctly. The identifier should be accessible in the class scope and properly linked to parent scopes.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently, not sure if it's related to recent changes in how class scopes are handled.

---
Repository: /testbed
