# Bug Report

### Describe the bug

I'm experiencing an issue with trailing slash handling when using paths that contain query parameters or hash fragments. The function seems to be extracting the wrong part of the URL when splitting on `#` or `?`.

### Reproduction

```js
const path = '/docs/intro?query=test#section';
const result = applyTrailingSlash(path, {
  trailingSlash: true,
  baseUrl: '/docs/'
});

// Expected: '/docs/intro/?query=test#section'
// Actual: The hash fragment '#section' is being used as the pathname instead of '/docs/intro'
```

When I pass a path with query parameters or hash fragments, it looks like the pathname extraction is getting the last segment after splitting instead of the first segment. This causes the trailing slash logic to operate on the wrong part of the URL.

### Expected behavior

The function should:
1. Extract the pathname (the part before `?` or `#`)
2. Apply trailing slash logic to the pathname
3. Preserve the query string and hash fragment in the correct positions

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
