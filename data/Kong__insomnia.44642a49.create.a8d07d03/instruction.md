# Bug Report

### Describe the bug
When trying to create a new unit test suite, I'm getting an error saying "New UnitTestSuite missing `parentId`" even though I'm providing the `parentId` in the patch object. This is preventing me from creating any test suites.

### Reproduction
```js
const testSuite = create({
  parentId: 'workspace_123',
  name: 'My Test Suite'
})
```

This throws an error:
```
Error: New UnitTestSuite missing `parentId` {"parentId":"workspace_123","name":"My Test Suite"}
```

### Expected behavior
The unit test suite should be created successfully when a valid `parentId` is provided. The error should only be thrown when `parentId` is actually missing or undefined.

### Additional context
This seems to have broken recently - I was able to create test suites before without any issues. The validation logic appears to be inverted somehow.

---
Repository: /testbed
