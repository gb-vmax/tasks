# Bug Report

### Describe the bug

After a recent update, I'm getting syntax errors when trying to remove documents from the database. The application fails to start and shows compilation errors related to the `unsafeRemove` function in the database module.

### Reproduction

```js
// Try to remove any document
const doc = await database.get('some-doc-id');
await database.unsafeRemove(doc);
```

The code doesn't even run - it fails during the build/compilation phase with syntax errors.

### Expected behavior

The `unsafeRemove` function should work as before, allowing documents to be removed from the database without removing their children. The code should at least compile and run.

### Additional context

Looking at the code, it seems like there might be a malformed function definition or duplicate code in the `unsafeRemove` method. The function appears to be declared twice or has some structural issue that's preventing the module from loading properly.

This is blocking our entire development workflow since the app won't even start now.

---
Repository: /testbed
