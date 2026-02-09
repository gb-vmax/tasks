# Bug Report

### Describe the bug

The `highlighter` function is returning an incorrect format when the `_highlight` parameter is `null` or `undefined`. Instead of returning the expected array of objects with `chunk` and `highlighted` properties, it's returning a plain array with just the string value.

### Reproduction

```js
import { highlighter } from '@mantine/core';

// When highlight is null/undefined, the function returns wrong format
const result = highlighter('some text', null);

console.log(result);
// Currently returns: ['some text']
// Expected: [{ chunk: 'some text', highlighted: false }]
```

This breaks any code that expects the standard format with `chunk` and `highlighted` properties.

### Expected behavior

The function should always return an array of objects with the structure `{ chunk: string, highlighted: boolean }`, even when `_highlight` is `null` or `undefined`. This maintains consistency with the return type for all other cases.

### System Info
- @mantine/core version: latest
- Browser: N/A (affects all environments)

---
Repository: /testbed
