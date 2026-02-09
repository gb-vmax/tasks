# Bug Report

### Describe the bug

The plugin filter logic seems to be inverted - files that should be filtered are being processed, and files that should be processed are being filtered out. When using `createFilterForTransform` with both `idFilter` and `codeFilter`, the behavior is completely backwards.

### Reproduction

```js
import { createFilterForTransform } from './utils/pluginFilter';

// Create a filter that should include .js files
const filter = createFilterForTransform(
  { include: ['**/*.js'] },
  undefined
);

// This returns false when it should return true
const shouldTransform = filter('test.js', 'some code');
console.log(shouldTransform); // Expected: true, Actual: false

// And files that should be excluded are being included
const filter2 = createFilterForTransform(
  { exclude: ['**/*.js'] },
  undefined
);

const shouldNotTransform = filter2('test.js', 'some code');
console.log(shouldNotTransform); // Expected: false, Actual: true
```

### Expected behavior

When a file matches the include pattern, the filter should return `true` to indicate it should be transformed. When a file matches the exclude pattern, it should return `false`.

Currently getting the opposite behavior - included files are being rejected and excluded files are being accepted.

---
Repository: /testbed
