# Bug Report

### Describe the bug

I'm encountering an issue with keyword token registration in the MDX parser. After a recent update, keyword tokens are not being stored correctly in the keywords registry, which is causing lookups to fail.

### Reproduction

When trying to use keyword tokens, the registration seems to be broken:

```js
// Create a keyword token
const myKeyword = kw('function', {});

// Try to look it up later
const retrieved = keywords['function'];  // This returns undefined now

// The token is actually stored under a different key
console.log(keywords['function_kw']);  // This has the token
```

The keyword is being registered with a modified key instead of the original keyword name, so subsequent lookups using the actual keyword name fail.

### Expected behavior

The keyword token should be registered using the original keyword name as the key, so that `keywords['function']` returns the correct token object. The lookup key should match the keyword name that was passed to `kw()`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is breaking keyword token resolution throughout the parser. Any code that expects to look up keywords by their name is now failing.

---
Repository: /testbed
