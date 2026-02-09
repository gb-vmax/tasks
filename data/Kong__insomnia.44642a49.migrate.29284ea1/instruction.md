# Bug Report

### Describe the bug

After a recent update, API spec documents are being migrated with an incorrect content type. When loading existing specs, the `contentType` field gets overwritten even when it was correctly set, causing specs to be interpreted as the wrong format.

### Reproduction

1. Create an API spec document with JSON content
2. Set the contentType to 'json'
3. Save and reload the document
4. The contentType gets changed to 'yaml' even though the content is valid JSON

Example content that triggers the issue:
```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "My API"
  }
}
```

The document contains the string "openapi:" within the JSON structure, which seems to be causing the migration logic to incorrectly detect it as YAML format.

### Expected behavior

The contentType should remain as 'json' since the content is valid JSON. The migration should not change an already-set contentType unless there's a clear mismatch.

### Additional context

This appears to be related to the new migration logic that tries to auto-detect content types. The detection is too aggressive and doesn't properly handle JSON content that happens to contain YAML-like keywords in its values.

---
Repository: /testbed
