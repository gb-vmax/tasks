# Bug Report

### Describe the bug
When using the automock functionality for gRPC services, the mock data generation is not working as expected. Instead of generating mock data based on the message type fields, empty objects are being returned.

### Reproduction
```js
// Set up a gRPC service with mocks enabled
const serviceMethods = {
  getUser: {
    requestType: UserRequest,
    responseType: UserResponse
  }
};

// Try to generate mock data for a method
const result = mockMethodReturnType(serviceMethods, MethodType.request, true);

// Expected: result.getUser() should return populated mock data
// Actual: result.getUser() returns { plain: {}, message: ... }
```

### Expected behavior
When mocks are enabled, the method should return properly populated mock data based on the message type fields. The `plain` property should contain the mocked field values, not an empty object.

### Additional context
This affects both request and response type mocking. The mock data generator seems to be skipped entirely when it should be generating data.

---
Repository: /testbed
