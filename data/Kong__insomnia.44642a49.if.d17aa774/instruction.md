# Bug Report

### Describe the bug

After a recent update, URL handling appears to be broken. When I try to make requests with valid URLs, I'm getting errors about the URL not being specified, even though I'm clearly passing a URL string.

### Reproduction

```js
// This used to work but now throws an error
const url = "http://example.com/api/test";
const urlObject = toUrlObject(url);
// Error: Request URL is not specified
```

The error message says the URL is not specified, but I'm definitely passing a valid URL string. This is breaking all my existing API calls that were working fine before.

### Expected behavior

The `toUrlObject` function should accept a valid URL string and convert it to a URL object without throwing errors. Previously this worked without issues.

### Additional context

This seems to have started happening after the latest changes. I noticed the function signature might have changed but I'm still passing the same type of arguments as before. The URL string is valid and non-empty, so I'm not sure why it's being rejected.

---
Repository: /testbed
