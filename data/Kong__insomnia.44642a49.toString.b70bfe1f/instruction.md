# Bug Report

### Describe the bug

When building a URL string using the `Url` object's `toString()` method, the query string is not being included in the output unless there's a hash fragment present. This breaks URL generation for cases where you have query parameters but no hash.

### Reproduction

```js
const url = new Url({
  protocol: 'https',
  host: 'example.com',
  path: '/api/endpoint',
  query: [
    { key: 'foo', value: 'bar' },
    { key: 'baz', value: 'qux' }
  ]
});

console.log(url.toString());
// Expected: https://example.com/api/endpoint?foo=bar&baz=qux
// Actual: https://example.com/api/endpoint
```

The query string just disappears from the URL if there's no hash. If I add a hash, then the query string shows up:

```js
url.hash = 'section';
console.log(url.toString());
// Output: https://example.com/api/endpoint?foo=bar&baz=qux#section
```

### Expected behavior

Query parameters should always be included in the URL string when present, regardless of whether a hash fragment exists or not.

### Additional context

This seems to have started happening recently. URLs without hashes used to work fine with query parameters.

---
Repository: /testbed
