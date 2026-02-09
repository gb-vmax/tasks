# Bug Report

### Describe the bug

When importing resources from a URI using the plugin API, subsequent imports from the same URI within the same session don't work. The import appears to be silently skipped even though the underlying resource may have changed.

### Reproduction

```js
// First import works fine
await context.data.import.uri('https://example.com/api-spec.yaml');

// Make changes to the remote resource at the URI
// ...

// Second import from the same URI is ignored
await context.data.import.uri('https://example.com/api-spec.yaml');
// Expected: Updated resource imported
// Actual: Nothing happens, old data remains
```

### Expected behavior

Each call to `context.data.import.uri()` should fetch and import the resource from the URI, even if the same URI was previously imported in the current session. If the remote resource has been updated, those changes should be reflected.

### Additional context

This seems to have started happening recently. Previously, calling the import function multiple times with the same URI would re-fetch and re-import the resource each time. This was useful for development workflows where the API spec is frequently updated.

It would be helpful to have a way to force re-import if caching behavior is intentional.

---
Repository: /testbed
