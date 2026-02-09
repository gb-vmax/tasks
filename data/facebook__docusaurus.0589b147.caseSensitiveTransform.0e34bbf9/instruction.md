# Bug Report

### Describe the bug

I'm experiencing an issue where certain HTML attributes are not being properly transformed in MDX. It seems like the attribute name mapping is broken - attributes that should be transformed to their correct names are instead returning undefined or incorrect values.

### Reproduction

```jsx
// When using attributes that need case transformation
<div className="test" data-value="hello" />

// Expected: attributes are properly mapped
// Actual: some attributes are returning undefined instead of their transformed names
```

The issue appears to be related to how attribute name lookups are performed. When an attribute exists in the transformation map but has a falsy value (like an empty string), it's not being handled correctly.

### Expected behavior

Attributes should be properly transformed according to the mapping, even when the mapped value is falsy. The function should check if the attribute key exists in the mapping object, not whether the mapped value is truthy.

### System Info
- MDX version: 3.0.0
- Node version: Latest

This seems to have broken after a recent change to the attribute transformation logic. The previous behavior was working correctly.

---
Repository: /testbed
