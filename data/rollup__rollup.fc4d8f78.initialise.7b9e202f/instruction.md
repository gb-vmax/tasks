# Bug Report

### Function declaration initialization order causes issues

I'm experiencing a problem where function declarations seem to be processed incorrectly, leading to unexpected behavior when the function's identifier is referenced before the function is fully initialized.

### Reproduction

```js
function myFunction() {
  // function body
}

// Accessing function identifier properties
```

When a function declaration is processed, the identifier's `isId` property is being set before the parent initialization completes. This causes issues when the function's scope or other properties need to be established first.

### Expected behavior

The function should be fully initialized (including all parent class initialization) before any identifier-specific properties are set. The identifier marking should happen after the base initialization is complete.

### Additional context

This seems to affect how function identifiers are tracked during the AST traversal phase. The timing of when `isId` is set on the variable matters for proper scope resolution.

---
Repository: /testbed
