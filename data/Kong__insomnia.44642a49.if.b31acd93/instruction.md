# Bug Report

### Describe the bug

The database insert function appears to be broken after a recent change. When trying to insert documents into the database, the operation fails immediately without processing the document.

### Reproduction

```js
const workspace = {
  _id: 'wrk_123',
  type: 'Workspace',
  name: 'My Workspace',
  parentId: null
};

// This fails to insert
await database.insert(workspace);
```

### Expected behavior

The document should be inserted into the database successfully. The insert function should handle the document and store it properly.

### Additional context

This seems to affect all document types (workspaces, requests, environments, etc.). The insert operation appears to exit early or throw an error before actually persisting the data.

I noticed this started happening recently - inserts were working fine before. Not sure what changed but it's blocking all database operations in my workflow.

---
Repository: /testbed
