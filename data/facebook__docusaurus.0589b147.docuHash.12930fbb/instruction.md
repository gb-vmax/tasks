# Bug Report

### Describe the bug

The `docuHash` function is generating incorrect hash filenames. When I pass in a root path `/`, it's not returning `'index'` as expected. Additionally, for longer paths, the function seems to be returning the shortened version even when the full kebab-cased path would fit within the filename length limit.

### Reproduction

```js
import { docuHash } from '@docusaurus/utils';

// This should return 'index' but doesn't
const hash1 = docuHash('/');
console.log(hash1); // Expected: 'index', Actual: something else

// For longer paths, getting shortened names when full names should work
const hash2 = docuHash('/some/normal/length/path');
console.log(hash2); // Getting shortened version unnecessarily
```

### Expected behavior

1. When the input is `'/'`, the function should return `'index'`
2. The function should only return the shortened version when the parsed path actually exceeds the OS filename length limit, not when it's within acceptable bounds

### System Info
- @docusaurus/utils version: latest
- Node: 18.x

---
Repository: /testbed
