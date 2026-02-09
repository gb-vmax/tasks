# Bug Report

### Describe the bug

The `getContentTypeName()` function is returning the wrong format (short vs long) based on the `useLong` parameter. When `useLong` is set to `true`, it returns the short name instead of the long name, and vice versa.

### Reproduction

```js
// This should return the long name but returns short name instead
const longName = getContentTypeName('application/json', true);
console.log(longName); // Expected: "JSON", Actual: "json"

// This should return the short name but returns long name instead
const shortName = getContentTypeName('application/json', false);
console.log(shortName); // Expected: "json", Actual: "JSON"
```

### Expected behavior

When `useLong` is `true`, the function should return the long/descriptive name for the content type. When `useLong` is `false` or omitted, it should return the short name.

For example:
- `getContentTypeName('application/json', true)` should return `"JSON"`
- `getContentTypeName('application/json', false)` should return `"json"`

### Additional context

This affects all content types handled by the function, including the fallback for `CONTENT_TYPE_OTHER`. The behavior is inverted from what the parameter name suggests.

---
Repository: /testbed
