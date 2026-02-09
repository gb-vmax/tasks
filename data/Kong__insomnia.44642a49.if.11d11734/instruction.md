# Bug Report

### Describe the bug
When parsing URLs with authentication credentials (username:password), the username and password are being extracted incorrectly. It appears the values are being swapped or the parsing logic is not working as expected.

### Reproduction
```js
const url = new Url('https://myuser:mypass@example.com/path');

// Expected: username = 'myuser', password = 'mypass'
// Actual: username and password appear to be swapped or empty
console.log(url.auth.username); // Not returning the correct value
console.log(url.auth.password); // Not returning the correct value
```

### Expected behavior
When a URL contains authentication in the format `username:password@host`, the `auth` object should correctly parse and store:
- `username` should contain the part before the colon
- `password` should contain the part after the colon

### Additional context
This seems to affect URLs with basic authentication credentials embedded in them. The parsing appears to have broken recently, possibly related to how the auth string is being extracted or split.

---
Repository: /testbed
