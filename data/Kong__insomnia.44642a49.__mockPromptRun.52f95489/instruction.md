# Bug Report

### Describe the bug

The `__mockPromptRun` function in the enquirer mock is not properly exporting the new helper functions and has a syntax error in the module.exports object. When trying to use the mock, the code fails because the object literal is malformed - there's a missing closing brace and the new const declarations are placed outside the exports object.

### Reproduction

```js
const enquirer = require('./__mocks__/enquirer');

// Try to use the mock
enquirer.__mockPromptRun('test value');

// This will fail because the module.exports is malformed
```

### Expected behavior

The mock should properly export all functions including the new helper functions like `__getCallHistory`, `__resetMock`, and `__getNextReturnValue`. The module.exports object should be properly structured with all exports accessible.

### Additional context

Looking at the mock file, it seems like the refactoring to add new functionality (call history tracking and multiple return values) introduced a syntax error. The const declarations for the helper functions are placed between the object properties, breaking the object literal syntax.

---
Repository: /testbed
