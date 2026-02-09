# Bug Report

### Describe the bug

After a recent update, API spec file extensions are being automatically changed when updating the spec contents, even when I don't want them to be. If I have a file named `my-api.yaml` and update its contents, the filename sometimes gets changed to `my-api.json` without me explicitly requesting it.

### Reproduction

```js
const apiSpec = {
  fileName: 'my-api.yaml',
  contentType: 'yaml',
  contents: 'openapi: 3.0.0\ninfo:\n  title: My API'
};

// Update just the contents
update(apiSpec, { 
  contents: '{"openapi": "3.0.0", "info": {"title": "My API"}}' 
});

// Expected: fileName stays as 'my-api.yaml'
// Actual: fileName gets changed to 'my-api.json'
```

The issue seems to happen when:
1. You have an existing API spec with a certain filename and content type
2. You update only the `contents` field
3. The file extension gets automatically changed based on the content format, even though `contentType` wasn't explicitly updated

### Expected behavior

The filename should only be modified when I explicitly change the `contentType` field or the `fileName` field. Just updating the contents shouldn't cause the file extension to change automatically.

If I want to keep my spec as YAML format but temporarily store JSON content, or vice versa, the system shouldn't force a filename change on me.

### System Info
- Version: latest
- OS: macOS

---
Repository: /testbed
