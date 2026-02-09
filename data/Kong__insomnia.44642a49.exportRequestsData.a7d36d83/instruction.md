# Bug Report

### Describe the bug

When exporting requests data, workspace documents are not being included in the exported resources. The export appears to complete successfully but workspace information is missing from the output.

### Reproduction

```js
// Export a workspace with requests
const exportData = await exportRequestsData(
  workspace,
  includePrivateDocs,
  format
);

// Check the exported resources
console.log(exportData.resources);
// Workspace is missing from the resources array
```

Steps to reproduce:
1. Create a workspace with some requests
2. Try to export the workspace data
3. Check the exported JSON/resources
4. Notice that workspace objects are not present in the export

### Expected behavior

The workspace should be included in the exported resources with `_type` set to the appropriate export type. All workspace data should be preserved in the export.

### Additional context

This seems to affect the entire export functionality - without the workspace being exported, the hierarchy of the exported data is incomplete. The export completes without errors but the resulting data structure is missing critical workspace information.

---
Repository: /testbed
