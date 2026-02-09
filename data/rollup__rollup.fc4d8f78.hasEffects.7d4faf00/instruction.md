# Bug Report

### Describe the bug

I'm encountering an issue where string concatenation expressions using the `+` operator are being incorrectly tree-shaken/removed from the output bundle. When I have a statement that concatenates an empty string with other values, it gets eliminated even though it should be preserved for its side effects.

### Reproduction

```js
// This statement gets removed from the bundle
'' + someValue;

// Expected: should be preserved in output
// Actual: gets tree-shaken away
```

The issue appears when you have an expression statement (not assigned to anything) that starts with an empty string literal and uses the `+` operator. This pattern is sometimes used to trigger type coercion or ensure side effects occur.

### Expected behavior

String concatenation expressions should be preserved in the output when they appear as standalone statements, as they can have side effects through type coercion (calling `toString()` methods, triggering getters, etc.).

### Additional context

This seems to have started happening recently. The bundler is treating these expressions as pure/side-effect-free when they actually aren't - the `+` operator can trigger implicit type coercion which may have observable side effects.

---
Repository: /testbed
