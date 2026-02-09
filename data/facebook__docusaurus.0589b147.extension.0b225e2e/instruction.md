# Bug Report

### Describe the bug

I'm encountering an issue with MDX extension merging where transforms are not being combined correctly. When multiple extensions with transforms are merged together, the resulting combined extension doesn't work as expected.

### Reproduction

```js
const extension1 = {
  transforms: [transform1, transform2]
};

const extension2 = {
  transforms: [transform3]
};

// After merging these extensions
const combined = extension(extension1, extension2);

// The transforms array structure is incorrect
// Expected: combined.transforms = [transform1, transform2, transform3]
// Actual behavior differs from expected
```

### Expected behavior

When merging extensions, all transforms from both extensions should be properly combined into a flat array. Each individual transform function should be added to the combined transforms array, not wrapped or nested in any way.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
