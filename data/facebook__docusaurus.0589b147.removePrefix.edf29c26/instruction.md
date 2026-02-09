# Bug Report

### Describe the bug

The `removePrefix()` function is not working as expected. When I pass a string with a matching prefix, the function returns the original string instead of removing the prefix. Conversely, when the prefix doesn't match, it tries to slice the string anyway which gives incorrect results.

### Reproduction

```js
import { removePrefix } from '@docusaurus/utils';

// This should return 'world' but returns 'hello-world'
const result1 = removePrefix('hello-world', 'hello-');
console.log(result1); // Expected: 'world', Actual: 'hello-world'

// This should return 'test' but returns 'st'
const result2 = removePrefix('test', 'foo-');
console.log(result2); // Expected: 'test', Actual: 'st'
```

### Expected behavior

When a string starts with the given prefix, `removePrefix()` should remove that prefix and return the remaining string. When the string doesn't start with the prefix, it should return the original string unchanged.

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
