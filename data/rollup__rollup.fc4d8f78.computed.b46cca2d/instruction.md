# Bug Report

### Describe the bug

I'm experiencing an issue with computed property keys in class definitions. When using computed property names (with square brackets), they're being treated as regular properties, and vice versa - regular property names are being treated as computed.

### Reproduction

```js
class MyClass {
  // Regular property - should NOT be computed
  regularProperty = 'value';
  
  // Computed property - should be computed
  ['computedProperty'] = 'value';
}
```

The behavior is inverted - `regularProperty` is being detected as computed, while `['computedProperty']` is being detected as non-computed. This is causing issues with property name resolution and code generation.

### Expected behavior

- Properties without square brackets should be identified as non-computed
- Properties with square brackets `[...]` should be identified as computed

This seems to have broken recently and is affecting how class properties are being processed.

---
Repository: /testbed
