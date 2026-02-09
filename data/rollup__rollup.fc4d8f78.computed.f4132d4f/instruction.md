# Bug Report

### Describe the bug

I'm encountering an issue with computed property definitions in class syntax. When defining a class with computed property names, the computed flag seems to be getting set incorrectly, causing the property to be treated as a regular property instead of a computed one.

### Reproduction

```js
class MyClass {
  [computedPropertyName] = value;
}
```

When parsing this code, the property should be marked as computed, but it appears the flag is not being set correctly. This causes issues with code generation and property access patterns.

### Expected behavior

Properties with computed names (using bracket notation) should be correctly identified and flagged as computed properties. The AST node should have `computed: true` for these cases.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
