# Bug Report

### Describe the bug

I'm experiencing an issue with HTTP response header parsing when dealing with non-standard or malformed responses. The application crashes or behaves unexpectedly when receiving responses that contain special characters, null bytes, or improperly formatted status lines.

### Reproduction

When making requests to certain servers that return responses with:
1. Binary data or null bytes in headers
2. Malformed status lines (missing parts, invalid status codes)
3. Non-ASCII characters in header values

The header parsing fails silently or produces incorrect results. For example:

```js
// Server returns a status line like "HTTP/1.1" (missing status code)
// Or "HTTP/1.1 abc OK" (non-numeric status code)
// Or headers containing null bytes or control characters

// Current behavior: parsing fails or returns unexpected values
// Expected: should handle gracefully with sensible defaults
```

### Expected behavior

The header parser should:
- Sanitize buffers containing null bytes and non-printable characters
- Handle malformed status lines gracefully (missing version, code, or reason)
- Return sensible defaults when status codes are invalid (non-numeric, out of range)
- Preserve valid extended ASCII characters (codes 128-255) while filtering out problematic ones

### Additional context

This seems to affect responses from legacy servers or proxies that don't strictly follow HTTP specifications. The current implementation assumes well-formed responses and doesn't validate the status line components properly.

System: Node.js environment with libcurl bindings

---
Repository: /testbed
