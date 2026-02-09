# Bug Report

### Describe the bug

When exporting requests, private documents are being included in the export even when `includePrivateDocs` is set to `false`. It seems like the logic for filtering private documents is inverted - documents marked as private are being exported when they shouldn't be.

### Reproduction

```js
// Export requests with includePrivateDocs = false
const exportData = await exportRequestsData(
  requests,
  false, // includePrivateDocs
  'json'
);

// Private documents (isPrivate = true) are still present in exportData.resources
// Expected: only non-private documents should be included
```

### Expected behavior

When `includePrivateDocs` is `false`, documents with `isPrivate = true` should be filtered out and not included in the export. Only non-private documents should be exported.

Currently, it appears the opposite is happening - private documents are being included while non-private ones might be getting filtered out.

### System Info
- Version: Latest
- Export format: JSON

---
Repository: /testbed
