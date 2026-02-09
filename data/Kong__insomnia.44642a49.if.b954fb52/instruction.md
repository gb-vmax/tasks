# Bug Report

### Describe the bug

I'm experiencing an issue with response body handling when the `bodyPath` is an empty string. The application is returning a buffer with unexpected content instead of an empty buffer.

### Reproduction

When a response object has a `bodyPath` set to an empty string (`''`), the current behavior returns a non-empty buffer:

```js
const response = {
  bodyPath: '',
  bodyCompression: undefined
}

const buffer = getBodyBuffer(response)
// Expected: Buffer with length 0
// Actual: Buffer with length 1
```

### Expected behavior

When `bodyPath` is an empty string (or missing), `getBodyBuffer` should return an empty `Buffer` with length 0, not a buffer with length 1. This is causing issues downstream where we check for empty response bodies.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
