# Bug Report

### Describe the bug

After a recent update, keywords are not being properly registered in the token type system. When trying to use keyword tokens, the system fails because it's storing the options object instead of the actual TokenType instance.

### Reproduction

```js
// Create a keyword token
const ifKeyword = kw('if', { beforeExpr: true });

// Try to access the keyword from the keywords registry
const registered = keywords['if'];

// Expected: registered should be a TokenType instance
// Actual: registered is just the options object without TokenType methods
console.log(registered instanceof TokenType); // false
console.log(registered.keyword); // 'if' (correct)
// But registered is missing all TokenType prototype methods
```

### Expected behavior

The `keywords` object should store actual `TokenType` instances, not just the options. The keyword tokens should have all the methods and properties of a proper TokenType.

### Additional context

This appears to affect all keyword definitions. The TokenType is being created but then discarded, with only the options object being stored in the registry instead.

---
Repository: /testbed
