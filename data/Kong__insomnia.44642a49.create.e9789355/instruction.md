# Bug Report

### Describe the bug

I'm experiencing an issue where request versions are being created incorrectly. It seems like the version creation logic is inverted - new versions are being created when there are NO changes to the request, and existing versions are being reused when there ARE changes.

### Reproduction

```js
// Create a request
const request = {
  type: 'Request',
  url: 'https://example.com',
  method: 'GET'
}

// Create initial version
const version1 = await create(request)

// Modify the request
request.url = 'https://example.com/api'

// Try to create a new version
const version2 = await create(request)

// Expected: version2 should be a NEW version with the updated URL
// Actual: version2 returns the OLD version (version1) without the changes
```

### Expected behavior

When a request is modified, calling `create()` should generate a new request version that captures the changes. When a request hasn't been modified, it should reuse the existing version to avoid duplicates.

Currently it's doing the opposite - it creates new versions for unchanged requests and reuses old versions when changes are detected.

### Additional context

This is causing issues with version history tracking. Changes to requests aren't being saved properly, and we're getting duplicate versions created unnecessarily when nothing has changed.

---
Repository: /testbed
