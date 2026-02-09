# Bug Report

### Describe the bug
When calling `mockRequestMethods()` with a `Service` and optional mocks parameter, the function is not working as expected. It seems like the arguments are being passed in the wrong order to `mockMethodReturnType()`, causing the mocking functionality to fail.

### Reproduction
```ts
const service = createService();

// This doesn't work correctly
mockRequestMethods(service, mockData);
```

The issue appears to be that `mockMethodReturnType` is receiving its arguments in an incorrect order - the `mocks` parameter and `MethodType.request` seem to be swapped.

### Expected behavior
The `mockRequestMethods()` function should properly pass the mocks and method type to `mockMethodReturnType()` in the correct order, allowing request methods to be mocked successfully.

### Additional context
This is affecting the automock functionality for request methods. The response methods variant (`mockResponseMethods`) seems to have the correct parameter order, so there's an inconsistency between the two functions.

---
Repository: /testbed
