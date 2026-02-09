# Bug Report

### Describe the bug

I'm experiencing an issue with `QueryParam` constructor when passing URL-encoded query parameter strings. The constructor seems to be failing or not properly handling encoded characters in query parameters.

### Reproduction

```js
// This works fine with JSON string
const param1 = new QueryParam('{"key":"test","value":"hello"}');

// But this fails with a regular query parameter string
const param2 = new QueryParam('name=John%20Doe');

// Also having issues with encoded special characters
const param3 = new QueryParam('email=user%40example.com');
```

When trying to create QueryParam objects from URL-encoded strings (like you'd get from parsing a URL's query string), the constructor throws an error or doesn't decode the values properly.

### Expected behavior

The QueryParam constructor should accept both:
1. JSON string format: `'{"key":"name","value":"test"}'`
2. URL query parameter format: `'key=value'` with proper URL decoding of encoded characters

For example:
- `'name=John%20Doe'` should decode to `key: 'name'`, `value: 'John Doe'`
- `'email=user%40example.com'` should decode to `key: 'email'`, `value: 'user@example.com'`
- `'flag'` (no equals sign) should work as `key: 'flag'`, `value: ''`

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This is blocking our ability to parse and work with query strings from URLs that contain encoded characters. Any help would be appreciated!

---
Repository: /testbed
