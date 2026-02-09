# Bug Report

### Describe the bug

When using case-insensitive attribute lookups, the wrong parameter is being lowercased. The attributes object is being lowercased instead of the property name, which causes attribute matching to fail.

### Reproduction

```js
const attributes = {
  'viewBox': '0 0 100 100',
  'preserveAspectRatio': 'xMidYMid'
}

// Try to lookup with different casing
const result = caseInsensitiveTransform(attributes, 'VIEWBOX')
// Expected: Should find 'viewBox' attribute
// Actual: Fails to match because attributes object is lowercased instead of property
```

### Expected behavior

The property parameter should be converted to lowercase for case-insensitive comparison, while the attributes object should remain unchanged. This would allow proper matching of attributes regardless of the casing used in the lookup.

### System Info
- MDX version: 3.0.0
- Affected component: property-information

---
Repository: /testbed
