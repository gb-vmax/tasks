# Bug Report

### Describe the bug

The `commondir` utility function is not correctly finding the common directory path when given an array of file paths. When I pass in multiple file paths, the function seems to be skipping or ignoring the first file path in the array when calculating the common ancestor directory.

### Reproduction

```js
import commondir from './utils/commondir';

const files = [
  '/home/user/project/src/index.js',
  '/home/user/project/src/utils/helper.js',
  '/home/user/project/src/components/App.js'
];

const result = commondir(files);
console.log(result);
// Expected: '/home/user/project/src'
// Actual: incorrect common directory (not considering the first file)
```

Another example with just two files:

```js
const files = [
  '/var/www/app/file1.js',
  '/var/www/app/file2.js'
];

const result = commondir(files);
// The first file path seems to be ignored in the comparison
```

### Expected behavior

The function should return the longest common directory path that is an ancestor to all provided file paths. All files in the input array should be considered when determining the common directory.

### Additional context

This appears to have started happening recently. The function works fine with a single file (returns its directory) but breaks down when multiple files are provided. It seems like the logic for comparing paths might not be including all files in the calculation.

---
Repository: /testbed
