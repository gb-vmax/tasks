# Bug Report

### Describe the bug

I'm encountering an issue with URL parsing when the auth section contains a username and password. The URL constructor is throwing an error for valid URLs that include authentication credentials.

### Reproduction

```js
const url = new Url('http://username:password@example.com/path');
// Error: new Url(): failed to parse auth in url http://username:password@example.com/path
```

The error is being thrown even though the URL format is valid and should properly parse the username and password from the auth section.

### Expected behavior

The URL should be parsed successfully, extracting `username` and `password` from the auth section without throwing an error. URLs with authentication credentials in the format `protocol://username:password@host` are standard and should be supported.

### Additional context

This seems to affect any URL that has both username and password in the auth section. URLs without auth or with just a username might work differently, but the standard format with both credentials is failing.

---
Repository: /testbed
