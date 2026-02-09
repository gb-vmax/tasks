# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with tokenizer exit handling in the remark parser. When tokens are being exited, the function returns the wrong value - it's returning the `type` parameter instead of the `token` object. This causes downstream code that expects to work with the returned token object to fail.

### Reproduction

```js
// When tokenizer exits a token
const tokenizer = createTokenizer(parser, initialize, from);
const token = tokenizer.exit2('someType');

// Expected: token should be the popped token object with 'end' property
// Actual: token is the string 'someType' instead of the token object
console.log(token); // 'someType' instead of { type: ..., start: ..., end: ... }
```

### Expected behavior

The `exit2` function should return the token object that was popped from the stack, not the type parameter. This is needed because calling code relies on getting the token object back to access its properties like `start`, `end`, and `type`.

### System Info
- remark version: 15.0.1
- Environment: Node.js

---
Repository: /testbed
