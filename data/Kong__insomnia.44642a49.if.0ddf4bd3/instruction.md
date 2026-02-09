# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with database updates in Insomnia. When trying to update documents, I'm getting syntax errors that prevent the application from working properly.

### Reproduction

```js
const doc = {
  _id: 'req_123',
  type: 'Request',
  name: 'My Request',
  // ... other properties
};

// Try to update the document
await database.update(doc);
```

The update operation fails immediately with a syntax error.

### Expected behavior

The document should be updated successfully without any syntax errors. The update function should validate the document and save it to the database.

### Additional context

This seems to have started happening after the latest changes to the database module. The application won't even start up properly now. Looking at the code, there appears to be a malformed function definition in the `database.update` method - the `_validateUpdate` function is defined outside of the main function body which causes a parsing error.

The function structure looks broken with improper nesting/indentation that makes the JavaScript invalid.

---
Repository: /testbed
