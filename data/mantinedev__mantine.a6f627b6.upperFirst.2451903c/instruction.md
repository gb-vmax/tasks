# Bug Report

### Describe the bug

The `upperFirst` utility function is not working correctly - it's returning the entire string in lowercase except for the first character, instead of just capitalizing the first letter.

### Reproduction

```js
import { upperFirst } from '@mantine/hooks';

const result = upperFirst('hello world');
console.log(result); // Expected: "Hello world"
console.log(result); // Actual: "Hhello world"
```

The function seems to be duplicating the first character instead of properly capitalizing just the first letter and keeping the rest of the string intact.

### Expected behavior

The function should capitalize only the first character of the string and leave the rest unchanged:
- `upperFirst('hello')` should return `'Hello'`
- `upperFirst('test string')` should return `'Test string'`
- `upperFirst('a')` should return `'A'`

### System Info
- @mantine/hooks version: latest
- Node version: 18.x

---
Repository: /testbed
