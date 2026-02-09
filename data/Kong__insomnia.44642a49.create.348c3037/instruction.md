# Bug Report

### Describe the bug

After a recent update, creating unit test suites is broken. The `create` function is now async but code that calls it isn't handling the promise correctly, causing test suites to not be created properly.

### Reproduction

```js
// This used to work but now fails
const suite = create({
  parentId: 'wrk_123',
  name: 'My Test Suite'
});

// suite is now a Promise instead of the created object
console.log(suite); // Promise { <pending> }
```

### Expected behavior

The function should either remain synchronous (as it was before) or existing callers should be updated to handle the async behavior. Currently, any code calling `create()` without `await` will receive a Promise instead of the actual UnitTestSuite object.

### Additional context

This appears to have broken after changes were made to add name uniqueness checking and sort key calculation. The function signature changed from synchronous to async, but this is a breaking change that affects all existing callers.

---
Repository: /testbed
