# Bug Report

### Describe the bug

I'm encountering an issue with object property parsing where numeric property keys are not being handled correctly. When defining object properties with numeric keys, they seem to be treated incorrectly which causes unexpected behavior in the parser.

### Reproduction

```js
const obj = {
  123: 'numeric key',
  name: 'regular key'
}

// The numeric property key (123) is not being processed as expected
```

When using numeric literals as object property keys, the parser appears to be misidentifying them, which leads to incorrect AST generation or property access issues.

### Expected behavior

Numeric property keys should be properly recognized and parsed. The object should be created with the numeric key accessible as expected, similar to how string keys work.

### Additional context

This seems related to how the parser distinguishes between different property key types (computed vs non-computed, numeric vs string identifiers). The issue manifests when working with object literals that contain numeric keys.

---
Repository: /testbed
