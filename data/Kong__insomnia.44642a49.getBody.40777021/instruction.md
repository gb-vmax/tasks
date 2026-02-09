# Bug Report

### Describe the bug

I'm experiencing an issue with the plugin response context where `getBody()` is returning decompressed content when the response has `content-encoding` headers (like gzip, deflate, or br). This is causing problems because the body is being automatically decompressed without any way to get the original raw body.

### Reproduction

```js
// When a response has content-encoding: gzip
const response = {
  headers: [
    { name: 'content-encoding', value: 'gzip' }
  ],
  body: '<gzipped binary data>'
}

// First call to getBody() returns decompressed content
const body1 = context.response.getBody()

// Second call also returns decompressed content (cached)
const body2 = context.response.getBody()

// But I need the raw gzipped body for further processing
```

The issue is that `getBody()` now automatically decompresses the response body based on the `content-encoding` header. This breaks existing plugins that expect to receive the raw body data and handle decompression themselves.

### Expected behavior

`getBody()` should return the raw body buffer without any automatic transformation. If decompression is needed, it should either:
1. Be opt-in via a separate method
2. Or be clearly documented that the body will be automatically decompressed

The current behavior is unexpected and breaks backward compatibility with existing plugins.

### Additional context

This appears to be using a WeakMap cache which means the decompressed body is cached on the first call, so there's no way to access the original compressed body after the first `getBody()` call.

---
Repository: /testbed
