# Bug Report

### Describe the bug

When updating an API spec's content type (e.g., switching from JSON to YAML), the file name extension doesn't automatically update to match the new content type. This causes a mismatch between the content type and file extension.

### Reproduction

```js
// Create or get an API spec with JSON content type
const spec = await getOrCreateForParentId(workspaceId);
// spec.fileName = 'my-api.json'
// spec.contentType = 'json'

// Update to YAML content type
await updateOrCreateForParentId(workspaceId, {
  contentType: 'yaml'
});

// Expected: fileName should be 'my-api.yaml'
// Actual: fileName remains 'my-api.json'
```

### Expected behavior

When the content type is changed, the file name extension should automatically update to match:
- Changing to `json` should ensure `.json` extension
- Changing to `yaml` should ensure `.yaml` or `.yml` extension

Additionally, if a user provides a fileName without an extension or with a mismatched extension, it should be normalized to match the content type.

### Additional context

This is particularly problematic when exporting or syncing specs, as the file extension doesn't reflect the actual content format.

---
Repository: /testbed
