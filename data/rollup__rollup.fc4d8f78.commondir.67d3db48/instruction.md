# Bug Report

### Describe the bug

I'm encountering an issue with the `commondir` utility function when it's given an array with only a single file path. The function appears to be using the wrong initial value for the reduce operation, causing it to skip the first file in the array.

### Reproduction

```js
import commondir from './utils/commondir';

// This returns an incorrect result
const result = commondir(['/path/to/file.js']);
console.log(result); // Expected: '/path/to', but getting unexpected behavior

// Also fails with multiple files where the first one matters
const result2 = commondir([
  '/app/src/index.js',
  '/app/src/utils/helper.js'
]);
console.log(result2); // Should consider the first file but doesn't
```

### Expected behavior

When passing a single file path, the function should return the directory portion of that path. When passing multiple files, all files (including the first one) should be considered when computing the common directory.

### Additional context

This seems to have started happening recently. The function works fine when there are multiple files and the first file happens to have the same directory structure as the others, but breaks when the first file is important for determining the common path.

---
Repository: /testbed
