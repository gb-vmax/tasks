# Bug Report

### Describe the bug

When calling `getBody()` multiple times in a plugin context, each call appears to be fetching/processing the response body independently instead of returning a cached version. This can cause performance issues and unexpected behavior when the same body needs to be accessed multiple times within a plugin script.

### Reproduction

```js
// In a plugin script
const response = await insomnia.request.send(config);

// First call to getBody
const body1 = response.getBody();

// Second call to getBody
const body2 = response.getBody();

// Each call seems to be processing the body independently
// This becomes problematic with large responses or when called frequently
```

### Expected behavior

The response body should be cached after the first `getBody()` call and subsequent calls should return the same buffer instance without reprocessing. This would improve performance and ensure consistent behavior across multiple accesses.

### Additional context

This is particularly noticeable when working with:
- Large response bodies
- Plugins that need to access the body multiple times
- Template rendering that references the response body in multiple places

---
Repository: /testbed
