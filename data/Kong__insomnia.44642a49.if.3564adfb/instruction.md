# Bug Report

### Describe the bug

I'm encountering an issue where providing a URL to a request is now causing an error to be thrown. The error message says "Request URL is not specified" even though I'm clearly passing a valid URL string.

### Reproduction

```js
const url = 'https://api.example.com/endpoint';
const urlObject = toUrlObject(url);
// Error: Request URL is not specified
```

This also happens when passing a Url object:

```js
const url = new Url('https://api.example.com/endpoint');
const urlObject = toUrlObject(url);
// Error: Request URL is not specified
```

### Expected behavior

The function should accept the URL and return a Url object without throwing an error. The error should only be thrown when the URL is actually missing or undefined.

### System Info

- insomnia-sdk version: latest
- Node version: 18.x

This seems to have started happening recently. Previously this code was working fine.

---
Repository: /testbed
