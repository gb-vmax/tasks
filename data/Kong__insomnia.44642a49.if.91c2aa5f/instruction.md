# Bug Report

### Describe the bug

The `filterHeaders` function is crashing when called with valid arguments. It appears that the validation logic for checking the headers parameter has an issue that causes it to fail when it should be working correctly.

### Reproduction

```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token' }
];

// This throws an error
const filtered = filterHeaders(headers, 'Content-Type');
```

The function throws: `TypeError: Cannot read property 'length' of undefined` or similar error when trying to filter headers with a valid array and name parameter.

### Expected behavior

The function should filter the headers array and return matching headers without throwing any errors. In the example above, it should return an array containing the Content-Type header.

### Additional context

This seems to have started happening recently. The function worked fine before but now fails even with valid input. The error occurs during the validation step before any actual filtering happens.

---
Repository: /testbed
