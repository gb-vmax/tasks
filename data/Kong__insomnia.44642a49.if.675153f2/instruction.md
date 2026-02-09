# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to update documents in the database. The application fails to start and crashes immediately when any database update operation is attempted.

### Reproduction

```js
const doc = {
  _id: 'some-id',
  type: 'request',
  name: 'My Request',
  modified: Date.now()
};

// This causes the app to crash
await database.update(doc);
```

### Expected behavior

The document should be updated successfully without any syntax errors. The update operation should complete normally and return the updated document.

### Additional context

This seems to have broken basic database functionality. The error appears to be related to the `update` function in the database module. Looking at the code, it seems like there might be a duplicate function definition or some structural issue with the update method.

The app was working fine before, but now it won't even start up properly.

---
Repository: /testbed
