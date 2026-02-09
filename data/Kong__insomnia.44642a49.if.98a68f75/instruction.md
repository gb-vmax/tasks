# Bug Report

### Describe the bug

After a recent update, I'm getting an error when trying to make requests without specifying a URL. Previously, this would throw a clear error message "Request URL is not specified", but now the behavior has changed and the error handling seems broken.

### Reproduction

```js
// This used to throw a clear error but now behaves unexpectedly
const urlObj = toUrlObject('');

// Also affects null/undefined cases
const urlObj2 = toUrlObject(null);
```

### Expected behavior

When an empty string, null, or undefined is passed to `toUrlObject()`, it should throw an error with the message "Request URL is not specified" to clearly indicate what went wrong.

### Additional context

This is causing issues in my request validation logic where I rely on catching this specific error to provide user feedback. The error handling for missing URLs seems to have been removed or changed in the latest version.

---
Repository: /testbed
