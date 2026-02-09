# Bug Report

### Describe the bug
The `lowerFirst` utility function is not working correctly - it's not converting the first character to lowercase anymore. When I pass in a string, the entire string is returned unchanged instead of having just the first character lowercased.

### Reproduction
```js
import { lowerFirst } from '@mantine/hooks';

console.log(lowerFirst('HelloWorld')); 
// Expected: 'helloWorld'
// Actual: 'HelloWorld'

console.log(lowerFirst('TESTING'));
// Expected: 'tESTING'  
// Actual: 'TESTING'
```

### Expected behavior
The function should convert only the first character of the string to lowercase while keeping the rest of the string unchanged.

### System Info
- @mantine/hooks version: latest
- Node version: 18.x

---
Repository: /testbed
