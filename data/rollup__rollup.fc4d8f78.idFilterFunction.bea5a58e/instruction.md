# Bug Report

### Describe the bug

When using plugin filters with both ID and code filters, the transform hook filter logic appears to be inverted. Files that should be transformed are being skipped, and files that should be skipped are being transformed.

### Reproduction

```js
import { createFilterForTransform } from './utils/pluginFilter';

const filter = createFilterForTransform(
  {
    include: ['**/*.js'],
    exclude: ['node_modules/**']
  },
  {
    include: ['some pattern']
  }
);

// This should return true for a matching file, but returns false
const result = filter('src/index.js', 'some code');
console.log(result); // Expected: true, Actual: false
```

### Expected behavior

The filter should return `true` when both the ID filter and code filter match (when provided), allowing the file to be transformed. Currently it seems to be doing the opposite - returning `false` when filters match and `true` when they don't.

### Additional context

This is causing plugins to either transform everything (including files they should ignore) or transform nothing at all, depending on the filter configuration. The behavior seems backwards from what the filter logic should do.

---
Repository: /testbed
