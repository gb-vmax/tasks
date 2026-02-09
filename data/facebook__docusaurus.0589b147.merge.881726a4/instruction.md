# Bug Report

### Describe the bug

After a recent update, HTML attribute normalization seems to be broken. When processing HTML elements with attributes, the attribute names and values are getting mixed up or not being handled correctly.

I'm working with rehype-stringify and noticed that attributes are not being normalized properly anymore. It looks like the property names and their normalized versions are being swapped somehow.

### Reproduction

```js
// When processing HTML with attributes like:
<div className="test" onClick="handler"></div>

// The normalized attribute names (class, onclick) and 
// property names (className, onClick) seem to be reversed
// Expected: className -> class normalization
// Actual: Getting incorrect mappings
```

### Expected behavior

Attributes should be correctly normalized between their property names (camelCase like `className`) and their normal HTML attribute names (lowercase like `class`). The schema merge should maintain the correct mapping between these two representations.

### System Info
- rehype-stringify: 10.0.0
- Node version: Latest

This seems to have started happening recently, possibly after some changes to the schema merging logic. The attribute normalization was working fine before.

---
Repository: /testbed
