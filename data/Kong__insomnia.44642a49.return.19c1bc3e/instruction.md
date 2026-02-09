# Bug Report

### Describe the bug

I'm experiencing an issue with URL query parameter manipulation. When trying to remove query parameters from a URL object, the code seems to be incomplete or broken. The `removeQueryParams` method doesn't work as expected and causes errors.

### Reproduction

```js
const url = new Url({
  protocol: 'https',
  host: ['example', 'com'],
  query: [
    { key: 'foo', value: 'bar' },
    { key: 'test', value: 'value' }
  ]
});

// Try to remove a query parameter
url.removeQueryParams('foo');
// This fails or doesn't work properly
```

Also trying with an array of parameter names:
```js
url.removeQueryParams(['foo', 'test']);
```

### Expected behavior

The `removeQueryParams` method should successfully remove the specified query parameters from the URL object. The remaining query parameters should still be accessible and the URL should be valid.

### Additional context

It looks like some of the URL helper methods like `getHost()`, `getPath()`, `getQueryString()`, etc. might also be affected or missing. The URL object doesn't seem to function correctly after recent changes.

---
Repository: /testbed
