# Bug Report

### Describe the bug

When exporting requests to HAR format, private environments are being incorrectly excluded from the export even when `includePrivateDocs` is set to true. The environment ID is being set to 'n/a' in cases where it should be using the actual environment.

### Reproduction

```js
// Setup
const workspace = { _id: 'ws_1', name: 'Test Workspace' };
const environment = { 
  _id: 'env_1', 
  isPrivate: true,
  data: { baseUrl: 'https://api.example.com' }
};
const requests = [/* array of requests */];

// Export with includePrivateDocs = true
await exportRequestsHAR(requests, true);

// Expected: Private environment should be included in HAR export
// Actual: Environment ID is set to 'n/a' and private environment data is excluded
```

### Expected behavior

When `includePrivateDocs` is set to `true`, private environments should be included in the HAR export. The environment ID should only be set to 'n/a' when:
- The environment doesn't exist, OR
- The environment is private AND `includePrivateDocs` is false

Currently it seems like the logic is inverted and private environments are being excluded even when they should be included.

### Additional context

This affects HAR exports for workspaces that use private environments. The exported HAR file is missing important environment configuration that should be present when explicitly requesting private docs to be included.

---
Repository: /testbed
