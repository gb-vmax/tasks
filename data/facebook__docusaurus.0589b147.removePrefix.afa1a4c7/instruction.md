# Bug Report

### Describe the bug

The `removePrefix()` function is not working as expected - it's removing text from the end of strings instead of from the beginning. When I try to remove a prefix from a string, the function doesn't do anything if the string starts with that prefix, but incorrectly removes text from the end if the string happens to end with it.

### Reproduction

```js
import { removePrefix } from '@docusaurus/utils';

// Expected: "world"
// Actual: "/hello/world" (nothing removed)
const result1 = removePrefix('/hello/world', '/hello/');

// Expected: "test" 
// Actual: "my-" (incorrectly removes from end)
const result2 = removePrefix('my-test', 'test');
```

### Expected behavior

`removePrefix(str, prefix)` should remove the prefix from the beginning of the string if it exists, otherwise return the original string unchanged.

For example:
- `removePrefix('/hello/world', '/hello/')` should return `'world'`
- `removePrefix('my-test', 'my-')` should return `'test'`
- `removePrefix('hello', 'bye')` should return `'hello'`

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
