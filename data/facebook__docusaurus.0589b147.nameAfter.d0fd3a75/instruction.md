# Bug Report

### Describe the bug

I'm experiencing an issue with directive attributes parsing where the attribute name token is not being properly closed before the initializer token is opened. This causes the token structure to be incorrect when parsing directives with attributes that have values.

### Reproduction

```js
// When parsing a directive like:
// ::directive{name="value"}

// The attribute name token should be exited before
// entering the initializer token, but currently
// the order is incorrect
```

The issue occurs when processing attributes with the `=` character (code 61). The token exit/enter sequence is happening in the wrong order, which breaks the expected token tree structure.

### Expected behavior

When parsing directive attributes with values, the tokens should be structured as:
1. Exit the attribute name token
2. Enter the initializer token  
3. Exit the initializer token
4. Consume the `=` character
5. Continue to value parsing

Currently, the consume happens before the exit, leading to malformed token sequences.

### System Info
- remark-directive version: 3.0.0
- This affects any directive using attributes with assigned values

---
Repository: /testbed
