# Bug Report

### Describe the bug

The `addSuffix()` function is adding the suffix even when the string already ends with it, causing duplicate suffixes to be appended.

### Reproduction

```js
import { addSuffix } from '@docusaurus/utils';

const result = addSuffix('myfile.md', '.md');
console.log(result); // Expected: 'myfile.md', Actual: 'myfile.md.md'
```

When calling `addSuffix` with a string that already has the desired suffix, the function incorrectly appends the suffix again instead of returning the string unchanged.

### Expected behavior

If the string already ends with the suffix, it should be returned as-is without appending the suffix again. The function should only add the suffix when it's not already present.

```js
addSuffix('myfile.md', '.md')  // Should return: 'myfile.md'
addSuffix('myfile', '.md')     // Should return: 'myfile.md'
```

### System Info
- @docusaurus/utils version: latest

---
Repository: /testbed
