# Bug Report

### Describe the bug

After a recent update, the cookie jar initialization seems to have broken. When creating a new cookie jar, I'm getting unexpected behavior where the `name` property is no longer a simple string and the `cookies` array appears to be `null` instead of an empty array.

### Reproduction

```js
const jar = init();

// This used to work but now fails
console.log(jar.name); // Expected: 'Default Jar', Got: { value: 'Default Jar', toString: ... }
console.log(typeof jar.name); // Expected: 'string', Got: 'object'

// This also breaks
jar.cookies.forEach(cookie => {
  // Process cookies
}); // TypeError: Cannot read property 'forEach' of null
```

### Expected behavior

- `jar.name` should be a string value `'Default Jar'`
- `jar.cookies` should be an empty array `[]`, not `null`

This is causing issues in our application where we iterate over cookies and expect the name to be a string for comparisons and display purposes.

### System Info
- Package: insomnia
- Version: latest

---
Repository: /testbed
