# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with project synchronization. When trying to sync projects, the `rootDocumentId` field is sometimes undefined instead of being set to the expected value. This causes downstream errors in the sync process.

### Reproduction

```js
// Create a project object
const project = {
  id: 'test-project',
  name: 'My Project'
}

// When syncing, rootDocumentId should be set but comes back as undefined
const schema = projectSchema.rootDocumentId()
console.log(schema) // Expected: 'rootDocumentId', Actual: undefined
```

### Expected behavior

The `rootDocumentId` should always return the string `'rootDocumentId'` consistently, regardless of the environment or window state. Currently it's returning `undefined` in certain scenarios which breaks project syncing.

### System Info
- Insomnia version: latest
- OS: Multiple (reproduced on Windows and macOS)

This seems to have started happening recently and is blocking our ability to sync projects properly. Any help would be appreciated!

---
Repository: /testbed
