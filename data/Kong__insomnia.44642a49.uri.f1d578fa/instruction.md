# Bug Report

### Describe the bug

After a recent update, the plugin data import functionality is broken. When trying to import data via URI, I'm getting an error about the URI format even though I'm passing valid URIs.

### Reproduction

```js
// This used to work but now throws an error
await context.data.import.uri('http://example.com/api/collection.json');

// Also fails with file paths
await context.data.import.uri('file:///path/to/collection.json');
```

The error message says something about invalid URI format, but the URIs look correct to me.

### Expected behavior

The import should work with valid HTTP/HTTPS/file URIs like it did before. The function should fetch the content and import it into the active project without throwing validation errors.

### Additional context

This started happening after the latest update. I'm using the plugin API to programmatically import collections, and this is blocking my workflow. The same URIs worked fine in the previous version.

---
Repository: /testbed
