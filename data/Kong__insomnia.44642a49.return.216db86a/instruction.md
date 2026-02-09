# Bug Report

### Describe the bug

After a recent update, URL query parameter removal methods are completely broken. When trying to use `removeQueryParams()` or any other URL manipulation methods like `getHost()`, `getPath()`, `getQueryString()`, etc., I'm getting errors because the methods seem to have been removed or corrupted.

### Reproduction

```js
const url = new Url('https://example.com/path?foo=bar&baz=qux');

// This should remove the 'foo' parameter
url.removeQueryParams('foo');

// This should return 'example.com'
const host = url.getHost();

// This should return the path
const path = url.getPath();
```

All of these operations fail now. The URL object seems to be missing critical methods.

### Expected behavior

- `getHost()` should return the host as a string (e.g., 'example.com')
- `getPath()` should return the path portion of the URL
- `getQueryString()` should return the formatted query string
- `removeQueryParams()` should properly remove specified query parameters
- Other URL helper methods should work as documented

### System Info

- insomnia-sdk version: latest
- Node version: 18.x

This is blocking our workflow as we rely heavily on URL manipulation in our pre-request scripts. Any help would be appreciated!

---
Repository: /testbed
