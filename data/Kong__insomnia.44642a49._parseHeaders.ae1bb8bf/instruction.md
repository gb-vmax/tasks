# Bug Report

### Describe the bug

After a recent update, HTTP response headers are being normalized to lowercase and duplicate headers (except `set-cookie`) are being aggregated into a single header with comma-separated values. This is causing issues when working with APIs that send multiple headers with the same name but expect them to remain separate.

### Reproduction

When making a request to an API that returns multiple headers with the same name:

```
HTTP/1.1 200 OK
Cache-Control: no-cache
Cache-Control: no-store
X-Custom-Header: value1
X-Custom-Header: value2
Set-Cookie: session=abc123
Set-Cookie: token=xyz789
```

The headers are now being transformed to:

```js
{
  'cache-control': 'no-cache, no-store',
  'x-custom-header': 'value1, value2',
  'set-cookie': 'session=abc123',
  'set-cookie': 'token=xyz789'
}
```

### Expected behavior

Headers should preserve their original casing and duplicate headers should remain as separate entries (not aggregated). Some protocols and APIs rely on the exact header names and expect duplicate headers to be kept separate, not combined with commas.

The original behavior was to keep headers as-is without normalization or aggregation.

### Additional context

This is particularly problematic for headers like `WWW-Authenticate` where multiple challenges need to remain separate, or custom headers where the API expects specific casing.

---
Repository: /testbed
