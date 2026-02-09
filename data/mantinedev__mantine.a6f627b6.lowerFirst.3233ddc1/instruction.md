# Bug Report

### Describe the bug

The `lowerFirst` utility function is returning an empty string for all valid string inputs instead of converting the first character to lowercase.

### Reproduction

```js
import { lowerFirst } from '@mantine/hooks';

console.log(lowerFirst('Hello')); // Expected: 'hello', Actual: ''
console.log(lowerFirst('World')); // Expected: 'world', Actual: ''
console.log(lowerFirst('TEST')); // Expected: 'tEST', Actual: ''
```

### Expected behavior

The function should convert the first character of the string to lowercase and keep the rest of the string unchanged:
- `lowerFirst('Hello')` should return `'hello'`
- `lowerFirst('World')` should return `'world'`
- `lowerFirst('TEST')` should return `'tEST'`

Currently, it's returning an empty string for all valid string inputs, which breaks any component or hook that relies on this utility function.

### System Info
- @mantine/hooks version: latest
- Node version: 18.x

---
Repository: /testbed
