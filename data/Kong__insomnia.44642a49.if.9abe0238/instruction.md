# Bug Report

### Describe the bug

The `getMostRecentlyModified` function appears to have duplicate code blocks after a recent change. When calling this function, I'm getting unexpected behavior where the function seems to be executing code twice or returning stale/incorrect results.

### Reproduction

```js
// Call getMostRecentlyModified to get the most recent document
const recentDoc = await database.getMostRecentlyModified('Request', {});

// Update a document
await database.update(someDoc);

// Call again - should return the updated document
const newRecentDoc = await database.getMostRecentlyModified('Request', {});

// The returned document doesn't reflect the latest changes
```

### Expected behavior

The function should return the most recently modified document of the specified type. After updating a document, subsequent calls should reflect those changes.

### Additional context

Looking at the code, it seems like there might be some merge conflict or accidental duplication in the `getMostRecentlyModified` function implementation. The function definition appears twice with different implementations, which is causing the runtime to behave unpredictably.

---
Repository: /testbed
