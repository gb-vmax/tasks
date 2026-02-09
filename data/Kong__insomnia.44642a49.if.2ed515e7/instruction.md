# Bug Report

### Describe the bug
When parsing URLs with authentication credentials, the username and password are being swapped. URLs that contain `username:password@host` are incorrectly assigning the password to the username field and vice versa.

### Reproduction
```js
const url = new Url('https://myuser:mypass@example.com/path');

console.log(url.auth.username); // Outputs: 'mypass' (expected: 'myuser')
console.log(url.auth.password); // Outputs: 'myuser' (expected: 'mypass')
```

Another example:
```js
const url = new Url('http://admin:secret123@api.example.com');
// username and password are reversed
```

### Expected behavior
The URL parser should correctly assign the username and password from the auth string. The format `username:password@host` should result in:
- `auth.username` = 'username'
- `auth.password` = 'password'

Currently they appear to be swapped.

---
Repository: /testbed
