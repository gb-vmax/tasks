# Bug Report

### Describe the bug
When using the `getBytesRead()` method in the plugin response context, it's returning incorrect values. The method seems to be returning a string instead of a number, and the calculation appears to be wrong.

### Reproduction
```js
// In a plugin script
const bytesRead = insomnia.response.getBytesRead();
console.log(typeof bytesRead); // Expected: 'number', Got: 'string'
console.log(bytesRead); // Shows unexpected concatenated string value
```

### Expected behavior
`getBytesRead()` should return a numeric value representing the actual number of bytes read from the response, not a string with concatenated values.

### System Info
- Insomnia version: latest
- OS: Various

---
Repository: /testbed
