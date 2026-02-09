# Bug Report

### Describe the bug

I'm experiencing an issue with parsing logic that seems to be inverted. When the parser encounters a token type that matches what it's looking for, it's behaving as if it doesn't match, and vice versa. This is causing unexpected parsing behavior in my MDX files.

### Reproduction

```js
// When parsing a token
// If the current token type matches the expected type:
// - It should consume the token (call next()) and return true
// - But instead it's returning false

// If the current token type does NOT match:
// - It should NOT consume the token and return false  
// - But instead it's consuming the token and returning true
```

This appears to be affecting the `eat()` method in the parser. The logic seems backwards - it's doing the opposite of what it should do based on whether the token type matches.

### Expected behavior

When checking if a token matches a specific type:
- If it matches: consume the token and return `true`
- If it doesn't match: don't consume the token and return `false`

### System Info
- @mdx-js/mdx version: 3.0.0
- This is breaking parsing for various MDX constructs

---
Repository: /testbed
