# Bug Report

### Describe the bug

When trying to export multiple workspaces to HAR format, the export fails with a type error. It seems like there's an issue with how the workspace documents are being processed before filtering for requests.

### Reproduction

```js
const workspaces = [workspace1, workspace2, workspace3];
await exportWorkspacesHAR(workspaces, false);
```

The function throws an error when trying to process the workspace documents. It appears that the filtering and flattening operations are happening in the wrong order, causing the subsequent operations to fail.

### Expected behavior

The function should:
1. Retrieve all documents from each workspace
2. Flatten the nested arrays
3. Filter for request documents only
4. Export them to HAR format

Instead, it's trying to filter before flattening, which doesn't work with nested arrays.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
