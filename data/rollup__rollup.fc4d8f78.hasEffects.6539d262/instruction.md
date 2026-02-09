# Bug Report

### Describe the bug

I'm encountering an issue where empty string concatenation using the `+` operator is being incorrectly tree-shaken/removed from my bundle. When I have code like `'' + someValue` at the top level, it's getting eliminated even though it should be preserved because it can cause side effects (type coercion errors at runtime).

### Reproduction

```js
// This statement is being removed from the bundle
'' + undefined;

// Expected: Should be preserved in output since it can throw
// Actual: Gets tree-shaken out
```

The issue occurs when:
1. Using the `+` operator with an empty string on the left side
2. The expression is a standalone statement (not assigned to anything)
3. The right operand could potentially cause a runtime error during coercion

### Expected behavior

Expressions like `'' + value` should be preserved in the output when they're standalone statements, as they can trigger runtime type coercion that might throw errors. The bundler should recognize these as having potential side effects.

### Additional context

This worked correctly in previous versions. It seems like the tree-shaking logic changed and now treats these expressions as pure/side-effect-free when they actually aren't.

---
Repository: /testbed
