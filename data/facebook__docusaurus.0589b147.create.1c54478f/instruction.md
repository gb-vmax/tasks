# Bug Report

### Describe the bug

I'm experiencing an issue with HTML attribute normalization in rehype-stringify. When working with properties that have different attribute names (like `className` -> `class`), the property lookup is returning the wrong values.

### Reproduction

```js
const schema = create({
  space: 'html',
  properties: {
    className: 'class'
  }
});

// Looking up normalized property name
const result = schema.normal['classname'];
// Expected: 'class'
// Actual: returns incorrect value
```

When I try to access normalized property names, I'm getting back the property name instead of the actual attribute name. This breaks attribute serialization in my HTML output.

### Expected behavior

The normalized lookup should return the correct attribute name. For example, looking up `'classname'` (normalized form of `className`) should return `'class'` (the actual HTML attribute), not `'className'`.

This is causing issues when rendering HTML elements because the wrong attribute names are being used in the output.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
