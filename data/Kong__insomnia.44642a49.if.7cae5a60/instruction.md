# Bug Report

### Describe the bug
After a recent update, URL parsing is failing for certain valid URL formats. The application throws errors when trying to process URLs that were previously working fine.

### Reproduction
```js
const url = "http://example.com/path";
const urlObj = toUrlObject(url);
// Error: Request URL is not specified
```

Also encountering issues with URLs that have certain formatting:
```js
const urlWithSpaces = "http://example.com /api/endpoint";
const result = toUrlObject(urlWithSpaces);
// Unexpected behavior or errors
```

### Expected behavior
Valid URLs should be parsed correctly without throwing errors. The `toUrlObject` function should handle standard URL formats and return proper Url objects.

### Additional context
This seems to have started happening recently. URLs that were working in previous versions are now causing errors. Not sure if this is related to some validation logic that was added or changed.

---
Repository: /testbed
