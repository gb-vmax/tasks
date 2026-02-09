# Bug Report

### Describe the bug

The `addSuffix()` function is not working as expected. When I try to add a suffix to a string, it's adding it in the wrong place or duplicating it.

### Reproduction

```js
import { addSuffix } from '@docusaurus/utils';

// This should add '/' at the end if it doesn't exist
const result1 = addSuffix('mypath', '/');
console.log(result1); // Expected: 'mypath/', Actual: '/mypath'

// This should return the string as-is since it already has the suffix
const result2 = addSuffix('mypath/', '/');
console.log(result2); // Expected: 'mypath/', Actual: 'mypath//'
```

### Expected behavior

- If the string doesn't end with the suffix, it should append the suffix at the end
- If the string already ends with the suffix, it should return the string unchanged

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
