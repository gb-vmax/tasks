# Bug Report

### Keyword token types not being reused correctly

I'm encountering an issue where keyword token types seem to be getting recreated instead of reusing the cached instances from the `keywords` object. This is causing problems with token type comparisons that rely on reference equality.

### Reproduction
```js
// Create two keyword tokens with the same name
const token1 = kw('if');
const token2 = kw('if');

// These should be the same instance but they're not
console.log(token1 === token2); // Expected: true, Actual: false
```

When the same keyword is requested multiple times, each call returns a new `TokenType` instance instead of returning the cached one from the `keywords` object. This breaks code that depends on token type identity checks.

### Expected behavior
The `kw()` function should return the same `TokenType` instance for a given keyword name on subsequent calls. The cached instance in the `keywords` object should be returned, not a newly created one.

### Additional context
This appears to affect the MDX parser's ability to correctly identify and compare keyword tokens during the parsing process.

---
Repository: /testbed
