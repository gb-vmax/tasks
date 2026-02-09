# Bug Report

### Describe the bug

The `upperFirst` utility function is not capitalizing the first letter of strings correctly. When I pass a string to the function, it returns an empty string instead of the string with its first character uppercased.

### Reproduction

```js
import { upperFirst } from '@mantine/hooks';

console.log(upperFirst('hello')); // Expected: 'Hello', Actual: ''
console.log(upperFirst('world')); // Expected: 'World', Actual: ''
console.log(upperFirst('test string')); // Expected: 'Test string', Actual: ''
```

### Expected behavior

The function should return the input string with the first character converted to uppercase. For example:
- `upperFirst('hello')` should return `'Hello'`
- `upperFirst('world')` should return `'World'`
- `upperFirst('test string')` should return `'Test string'`

Currently it just returns an empty string for all valid string inputs.

---
Repository: /testbed
