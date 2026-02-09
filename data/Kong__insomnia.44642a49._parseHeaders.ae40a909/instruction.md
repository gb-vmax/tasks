# Bug Report

### Describe the bug

After a recent update, HTTP response headers are not being parsed correctly when the status line contains unusual spacing or malformed HTTP version strings. The parser seems to have issues with edge cases that previously worked.

### Reproduction

When making requests that return responses with:
1. Multiple spaces between status line components (e.g., `HTTP/1.1  200  OK`)
2. Non-standard HTTP version formats (e.g., `HTTP/2` without the decimal)
3. Missing or empty reason phrases

The header parsing fails or returns incorrect values. For example:

```
HTTP/2 404
Content-Type: application/json
```

This response should parse correctly with code `404` and an appropriate default reason phrase, but instead the parser may return code `0` or an invalid status.

### Expected behavior

The header parser should handle:
- Variable whitespace in status lines
- Different HTTP version formats (HTTP/1.1, HTTP/2, HTTP/3, etc.)
- Missing reason phrases (should use default phrases for common status codes)
- Gracefully degrade for malformed status lines instead of failing completely

### Additional context

This appears to affect requests to servers that don't strictly follow HTTP/1.1 formatting conventions. Some proxy servers and CDNs use condensed status line formats that are technically valid but don't match the typical spacing pattern.

---
Repository: /testbed
