# Bug Report

### Describe the bug

The `upperFirst` utility function is not capitalizing strings correctly. It seems to be missing the first character after capitalization.

### Reproduction

```js
import { upperFirst } from '@mantine/hooks';

console.log(upperFirst('hello'));
// Expected: 'Hello'
// Actual: 'Hllo'

console.log(upperFirst('test'));
// Expected: 'Test'  
// Actual: 'Tst'

console.log(upperFirst('a'));
// Expected: 'A'
// Actual: 'A'

console.log(upperFirst('world'));
// Expected: 'World'
// Actual: 'Wrld'
```

### Expected behavior

The function should capitalize the first letter and keep all other characters intact. For example, `upperFirst('hello')` should return `'Hello'`, not `'Hllo'`.

### System Info

- @mantine/hooks version: latest
- Node version: 18.x

---
Repository: /testbed
