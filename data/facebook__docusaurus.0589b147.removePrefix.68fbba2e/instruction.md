# Bug Report

### Describe the bug

The `removePrefix()` function is not working correctly - it's not actually removing the prefix from strings. Instead, it seems to be checking the parameters in the wrong order and returning unexpected results.

### Reproduction

```js
import { removePrefix } from '@docusaurus/utils';

// Expected: "world"
// Actual: "helloworld"
const result1 = removePrefix('helloworld', 'hello');
console.log(result1); // Returns the original string unchanged

// Expected: "bar"
// Actual: "foobar"
const result2 = removePrefix('foobar', 'foo');
console.log(result2); // Also returns the original string
```

### Expected behavior

When calling `removePrefix(str, prefix)`, it should remove the prefix from the beginning of the string if it exists. For example:
- `removePrefix('helloworld', 'hello')` should return `'world'`
- `removePrefix('foobar', 'foo')` should return `'bar'`
- `removePrefix('test', 'xyz')` should return `'test'` (no prefix to remove)

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is blocking our ability to properly process URL paths and file names in our build pipeline. Any help would be appreciated!

---
Repository: /testbed
