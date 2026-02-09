# Bug Report

### Describe the bug

I'm experiencing an issue with attribute handling in MDX where attributes are not being resolved correctly. When using attributes that should be case-sensitive, the transform function is returning unexpected values.

### Reproduction

```js
const attributes = {
  'viewBox': 'viewBox',
  'className': 'className'
}

// Trying to get the correct attribute name
const result = caseSensitiveTransform(attributes, 'viewBox')

// Expected: 'viewBox'
// Actual: 'viewBox' is returned when attribute exists in the map
// But when attribute doesn't exist, it tries to access attributes[attribute] 
// which returns undefined instead of the original attribute
```

The issue seems to be with how the function determines whether to use the mapped value or the original attribute. When an attribute is NOT in the attributes map, it should return the original attribute name, but instead it's trying to look it up in the map.

### Expected behavior

- If an attribute exists in the mapping, return the mapped value
- If an attribute doesn't exist in the mapping, return the original attribute name as-is

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing SVG attributes and other case-sensitive HTML attributes to not work properly in MDX components.

---
Repository: /testbed
