# Bug Report

### Describe the bug

The `lowerFirst` utility function is not working correctly - it only returns the first character in lowercase instead of the full string with the first character lowercased.

### Reproduction

```js
import { lowerFirst } from '@mantine/hooks';

const result = lowerFirst('HelloWorld');
console.log(result); // Expected: 'helloWorld', Actual: 'h'

const result2 = lowerFirst('TestString');
console.log(result2); // Expected: 'testString', Actual: 't'
```

### Expected behavior

The function should return the entire string with only the first character converted to lowercase, not just the first character alone.

For example:
- `lowerFirst('HelloWorld')` should return `'helloWorld'`
- `lowerFirst('TestString')` should return `'testString'`
- `lowerFirst('ABC')` should return `'aBC'`

Currently it's only returning the first character.

### System Info
- @mantine/hooks version: latest
- Node: 18.x

---
Repository: /testbed
