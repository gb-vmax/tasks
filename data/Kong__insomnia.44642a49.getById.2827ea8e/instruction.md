# Bug Report

### Describe the bug

I'm experiencing an issue where request IDs are being corrupted when retrieved through the templating system. The request ID appears to have duplicate characters appended to it, which causes lookups and references to fail.

### Reproduction

```js
// Get a request by ID through the template context
const request = await context.util.models.request.getById('req_123abc');

// Expected ID: 'req_123abc'
// Actual ID: 'req_123abcc' (notice the extra 'c' at the end)
console.log(request.id); // outputs: 'req_123abcc'
```

The ID seems to have the last character duplicated and appended. This breaks any downstream operations that depend on the correct request ID.

### Expected behavior

The `getById` method should return the request object with its original, unmodified ID. The ID should remain exactly as it was stored, without any additional characters appended.

### Additional context

This is causing issues in our workflow where we reference requests by ID in templates. The corrupted IDs mean we can't properly link or reference requests, and any subsequent lookups using the returned ID fail since the ID no longer matches what's in the database.

---
Repository: /testbed
