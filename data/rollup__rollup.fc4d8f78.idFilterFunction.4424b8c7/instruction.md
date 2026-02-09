# Bug Report

### Describe the bug

I'm encountering unexpected behavior with the plugin filter system. When I configure both an `idFilter` and a `codeFilter`, the filtering logic seems to be inverted or not working as expected. Files that should be excluded are being processed, and the filter appears to always return `true` regardless of the filter conditions.

### Reproduction

```js
import { createFilterForTransform } from './utils/pluginFilter';

const filter = createFilterForTransform(
  {
    include: ['**/*.js'],
    exclude: ['**/node_modules/**']
  },
  {
    include: ['somePattern']
  }
);

// This should return false for node_modules files, but returns true
const result = filter('node_modules/package/file.js', 'some code');
console.log(result); // Expected: false, Actual: true
```

### Expected behavior

When a file ID doesn't match the `idFilter` criteria (e.g., it's in an excluded path), the filter should return `false` and prevent further processing. The combined filter should only return `true` when both the ID and code filters pass (if both are defined).

### Additional context

This seems to affect the transform hook filtering mechanism. Files that should be skipped based on the filter configuration are being transformed anyway, which impacts build performance and can cause unexpected side effects.

---
Repository: /testbed
