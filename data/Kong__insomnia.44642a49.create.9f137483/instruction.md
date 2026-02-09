# Bug Report

### Describe the bug

I'm experiencing an issue when creating a new unit test suite. The function appears to be checking and passing incorrect parameters, which causes the suite creation to fail or behave unexpectedly.

### Reproduction

```js
// Trying to create a unit test suite with proper parameters
const suite = create({
  parentId: 'wrk_123',
  name: 'My Test Suite',
  // other properties...
})
```

When I call the create function with a valid patch object containing `parentId` and other properties, it doesn't work as expected. The validation seems off and the data being passed to the database creation function doesn't match what I'm providing.

### Expected behavior

The function should:
1. Validate that `patch.parentId` exists in the provided patch object
2. Pass the entire patch object to `db.docCreate()` so all properties are properly stored

Instead, it seems like the validation and the actual data being passed aren't aligned with what the function should be doing.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
