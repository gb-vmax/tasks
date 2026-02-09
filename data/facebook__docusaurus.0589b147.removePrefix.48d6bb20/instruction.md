# Bug Report

### Describe the bug

The `removePrefix()` utility function is not removing the prefix correctly from strings. When I pass a string with a known prefix, the function returns an incorrect result with part of the prefix still remaining.

### Reproduction

```js
import {removePrefix} from '@docusaurus/utils';

const result = removePrefix('myPrefix-content', 'myPrefix-');
console.log(result); // Expected: 'content', Actual: 'ontent'
```

The prefix is mostly removed but the last character of the prefix ('t' in this case) gets included in the result, causing the first character of the remaining string to be cut off.

### Expected behavior

The function should completely remove the prefix and return only the remaining part of the string. For example:
- `removePrefix('hello-world', 'hello-')` should return `'world'`
- `removePrefix('test', 'te')` should return `'st'`
- `removePrefix('noprefix', 'other')` should return `'noprefix'` (unchanged)

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
