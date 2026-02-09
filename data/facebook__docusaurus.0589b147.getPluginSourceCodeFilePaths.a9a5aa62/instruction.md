# Bug Report

### Describe the bug

Getting an error when trying to extract translations from plugin source code. The extraction process crashes when a plugin doesn't define `getPathsToWatch()` or returns `undefined`.

### Reproduction

Create a plugin without implementing `getPathsToWatch()`:

```js
const myPlugin = {
  name: 'my-custom-plugin',
  getThemePath() {
    return './theme';
  }
  // Note: getPathsToWatch() is not defined
};
```

When the translation extraction runs, it throws an error because it tries to call `.map()` on `undefined`.

### Expected behavior

The extraction should handle plugins that don't implement `getPathsToWatch()` gracefully, falling back to an empty array or only using the theme path if available.

### Additional context

This seems to have started happening recently. Previously the code had a fallback (`?? []`) that would handle this case, but it looks like that might have been removed or changed.

---
Repository: /testbed
