# Bug Report

### Describe the bug

The `getContentTypeName` function is not returning the correct content type name anymore. It seems to always return an empty string now, even for valid content types that should match.

### Reproduction

```js
import { getContentTypeName } from './constants';

// This should return 'JSON' but returns ''
const result1 = getContentTypeName('application/json');
console.log(result1); // Expected: 'JSON', Actual: ''

// This should return 'XML' but returns ''
const result2 = getContentTypeName('application/xml');
console.log(result2); // Expected: 'XML', Actual: ''

// Even with charset parameter
const result3 = getContentTypeName('application/json; charset=utf-8');
console.log(result3); // Expected: 'JSON', Actual: ''
```

### Expected behavior

The function should return the appropriate content type name (short or long version depending on the `useLong` parameter) when a matching content type is found. For example:
- `'application/json'` should return `'JSON'`
- `'text/html'` should return `'HTML'`
- etc.

This was working fine before but now all content types just return empty strings.

---
Repository: /testbed
