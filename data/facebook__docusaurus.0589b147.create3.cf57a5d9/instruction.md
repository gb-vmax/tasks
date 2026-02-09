# Bug Report

### Describe the bug

I'm experiencing issues with property normalization in the schema creation logic. When working with attribute definitions, the normalized attribute names are not being mapped correctly, which causes lookups to fail for certain properties.

### Reproduction

```js
// Create a schema with properties that have custom attributes
const schema = create3({
  properties: {
    className: {
      attribute: 'class'
    },
    htmlFor: {
      attribute: 'for'
    }
  },
  space: 'html'
});

// Try to access normalized property
// Expected: should find the property by normalized attribute name
// Actual: returns undefined or incorrect mapping
```

### Expected behavior

When normalizing attribute names, the schema should correctly map both the property name and the attribute name to their corresponding property definitions. Looking up a property by its normalized attribute name should work as expected.

### Additional context

This seems to affect how properties are indexed in the schema's normal mapping object. The iteration and assignment logic appears to have some inconsistencies that prevent proper attribute resolution.

---
Repository: /testbed
