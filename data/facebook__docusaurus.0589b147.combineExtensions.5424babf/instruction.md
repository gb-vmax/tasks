# Bug Report

### Describe the bug

I'm experiencing an issue with the `combineExtensions` function where it's not properly initializing the combined extensions object. The function seems to be setting an initial `length` property on the object which causes unexpected behavior when combining syntax extensions.

### Reproduction

```js
const extensions = [
  { /* extension 1 */ },
  { /* extension 2 */ }
];

const combined = combineExtensions(extensions);
// The combined object has an unexpected 'length: 0' property
// This interferes with normal object operations
```

When I inspect the returned object, it has a `length` property set to `0` that shouldn't be there. This seems to be treating the object like an array when it should be a plain object for storing extension properties.

### Expected behavior

The `combineExtensions` function should return a plain object without any pre-initialized properties. The object should only contain the merged properties from the input extensions, not a `length` property.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
