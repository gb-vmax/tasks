# Bug Report

### Describe the bug

I'm encountering an issue where computed property keys in class methods are not being recognized correctly. When defining methods with computed property names (using bracket notation), the bundler seems to be treating them incorrectly, which affects the generated output.

### Reproduction

```js
class MyClass {
  [Symbol.iterator]() {
    // method implementation
  }
  
  ['computed' + 'Name']() {
    // method implementation  
  }
}
```

When bundling code with computed method names like the above, the methods are not handled as expected. The computed property detection appears to be broken.

### Expected behavior

Methods with computed property keys (defined using bracket notation) should be properly identified and processed during bundling. The `computed` property getter should return `true` for these methods.

### Additional context

This seems to affect any method definition that uses computed property names, including:
- Symbol-based method names
- Dynamic property names using template expressions
- Any bracket notation for method keys

The issue appears to be in how the AST node determines whether a method key is computed or not.

---
Repository: /testbed
