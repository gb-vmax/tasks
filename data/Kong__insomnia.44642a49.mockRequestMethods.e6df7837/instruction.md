# Bug Report

### Describe the bug

I'm experiencing an issue with the automocking functionality where request methods are not being mocked correctly. When I try to mock request methods on a service, the mocks don't seem to be applied properly and the behavior is unexpected.

### Reproduction

```js
const service = createService({
  // service configuration
});

const mocks = {
  getUserData: jest.fn().mockResolvedValue({ id: 1, name: 'Test User' })
};

const mockedService = mockRequestMethods(service, mocks);

// Expected: getUserData should return mocked value
// Actual: Mocks don't seem to be applied correctly
```

### Steps to reproduce:
1. Create a service with request methods
2. Define mocks for the request methods
3. Call `mockRequestMethods()` with the service and mocks
4. Try to use the mocked methods

### Expected behavior

Request methods should be properly mocked with the provided mock implementations. The mocked service should use the mock functions instead of the actual implementations.

### Additional context

This seems to have started happening recently. The mocks are passed in correctly but they don't seem to take effect. Not sure if this is related to how empty mock objects are handled or something else.

---
Repository: /testbed
