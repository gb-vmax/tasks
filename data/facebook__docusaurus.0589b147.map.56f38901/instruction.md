# Bug Report

### Describe the bug

I'm experiencing an issue with object merging in remark where properties are being unexpectedly deleted from objects before they're reassigned. This seems to be affecting the internal state management.

### Reproduction

```js
const original = {
  type: 'paragraph',
  children: [],
  position: { start: { line: 1 } }
}

const updates = {
  children: [{ type: 'text', value: 'hello' }]
}

// After merging, original object loses properties it should keep
merge(original, updates)

// Expected: original should have type, children, and position
// Actual: original only has properties from updates
```

### Expected behavior

When merging objects, the target object should retain properties that aren't being overwritten. Only properties present in the source object should be updated, not all existing properties deleted first.

### Additional context

This appears to affect the AST node processing. When nodes are being updated with new properties, they're losing their existing metadata and structure that should be preserved.

---
Repository: /testbed
