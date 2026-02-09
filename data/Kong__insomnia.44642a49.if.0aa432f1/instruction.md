# Bug Report

### Describe the bug

I'm experiencing an issue with JSON prettification where escape sequences in strings are being duplicated. When prettifying JSON that contains escaped characters like `\"` or `\\`, the output includes the escape sequences twice, resulting in malformed JSON.

### Reproduction

```js
const jsonString = '{"message": "Hello \\"World\\""}';
const prettified = jsonPrettify(jsonString);
console.log(prettified);
// Output: {"message": "Hello \\"World\\""}
// Expected: {"message": "Hello \"World\""}
```

Another example with backslashes:

```js
const jsonString = '{"path": "C:\\\\Users\\\\test"}';
const prettified = jsonPrettify(jsonString);
// The backslashes get duplicated incorrectly
```

### Expected behavior

The prettified JSON should maintain the correct escape sequences without duplication. Escaped quotes, backslashes, and other special characters should be preserved properly in the output.

### System Info
- Version: latest
- This seems to have started happening recently, possibly after a recent update to the prettify logic

---
Repository: /testbed
