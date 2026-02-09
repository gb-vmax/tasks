# Bug Report

### Describe the bug

I'm experiencing an issue with attribute handling in MDX where case-insensitive attribute lookups are failing. It seems like attributes are being transformed incorrectly, causing the lookup mechanism to break.

### Reproduction

```js
const attributes = {
  'dataValue': 'test',
  'className': 'my-class'
}

// Trying to look up case-insensitive properties
const result = caseInsensitiveTransform(attributes, 'DataValue')
// This throws an error or returns undefined instead of finding the attribute
```

When working with HTML/JSX attributes that should be case-insensitive, the transformation logic appears to be applying the case conversion to the wrong parameter. This causes attribute lookups to fail even when the attribute exists in the object.

### Expected behavior

Case-insensitive attribute lookups should work correctly regardless of the casing used. The function should be able to find `dataValue` when searching for `DataValue`, `DATAVALUE`, etc.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken attribute resolution for standard HTML attributes that should be case-insensitive according to the spec.

---
Repository: /testbed
