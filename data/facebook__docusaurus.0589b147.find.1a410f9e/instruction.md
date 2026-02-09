# Bug Report

### Describe the bug
I'm experiencing issues with data attributes handling in MDX. When using custom data attributes with dashes (like `data-test-value`), they're not being processed correctly. The attribute names seem to be getting mangled or incorrectly transformed.

### Reproduction
```jsx
// Using a data attribute with a dash prefix
<div data-test-value="hello" />

// Also seeing issues with camelCase data attributes
<div dataTestValue="world" />
```

After rendering, the attributes don't appear as expected in the output. It looks like the transformation logic for data attributes is broken.

### Expected behavior
Data attributes should be properly normalized and transformed:
- `data-test-value` should work correctly
- `dataTestValue` should be converted to the proper format
- The dash handling in attribute names should work as documented

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently, as it was working fine before. Not sure if this is related to recent changes in the attribute normalization code.

---
Repository: /testbed
