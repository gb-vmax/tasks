# Bug Report

### Describe the bug

The `createFilterForTransform` function is not working correctly when both `idFilter` and `codeFilter` are provided. It seems like the filter logic is inverted - when the ID filter matches, it returns `false` instead of continuing to check the code filter.

### Reproduction

```js
import { createFilterForTransform } from './utils/pluginFilter';

const filter = createFilterForTransform(
  {
    include: ['**/*.js'],
    exclude: ['node_modules/**']
  },
  {
    include: ['somePattern']
  }
);

// This returns false even though the ID matches the filter
const result = filter('src/test.js', 'some code with somePattern');
console.log(result); // Expected: true, Actual: false
```

### Expected behavior

When both ID and code filters are provided:
1. If the ID filter matches, it should proceed to check the code filter
2. Only return `true` if both filters match (or if only one is provided and it matches)
3. The filters should work in an AND relationship, not return early with inverted logic

Currently it appears that passing the ID filter causes the function to immediately return `false`, which doesn't make sense for a filtering function.

### System Info
- Version: latest
- Node: 18.x

---
Repository: /testbed
