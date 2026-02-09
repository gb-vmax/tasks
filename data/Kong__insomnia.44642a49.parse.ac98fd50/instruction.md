# Bug Report

### Describe the bug

Query parameter parsing is broken when using the standard `UrlSearchParams` approach. The parser is now attempting to extract type information from keys using a colon delimiter (e.g., `key:type`), but this breaks compatibility with standard URL query strings that may legitimately contain colons in their keys.

### Reproduction

```js
// This query string should parse correctly
const queryStr = "time:stamp=123456&user:id=abc&normal=value";

const params = QueryParam.parse(queryStr);

// Expected: 
// [
//   { key: 'time:stamp', value: '123456' },
//   { key: 'user:id', value: 'abc' },
//   { key: 'normal', value: 'value' }
// ]

// Actual behavior: Keys are being split at colons and treated as type annotations
// This breaks existing query strings with colons in the key names
```

### Expected behavior

The parser should handle standard URL query strings without trying to interpret colons as special type delimiters. Query parameters with colons in their keys should be preserved as-is, just like the previous implementation using `UrlSearchParams`.

### Additional context

This appears to have started after a recent change to the `QueryParam.parse()` method. The previous implementation correctly handled all valid URL query string formats. The new custom parsing logic with type extraction is causing regressions for standard query strings.

---
Repository: /testbed
