# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with document upserts in the database. When trying to upsert documents, I'm getting syntax errors that prevent the application from running properly. It looks like there's a problem with the upsert function definition.

### Reproduction

```js
const doc = {
  _id: 'test-123',
  type: 'request',
  name: 'My Request',
  modified: Date.now()
};

// Attempting to upsert the document
await database.upsert(doc);
```

### Expected behavior

The upsert operation should complete successfully, either inserting a new document or updating an existing one without any syntax errors.

### Additional context

This appears to have started happening after some changes to the database module. The application fails to start and I'm seeing parsing errors related to the database code. It seems like there might be duplicate or malformed function definitions in the upsert method.

---
Repository: /testbed
