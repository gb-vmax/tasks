# Bug Report

### Describe the bug

The `mockRequestMethods` function in the automock IPC module isn't working as expected. When trying to mock request methods, the mocking doesn't seem to be applied correctly and the behavior is inconsistent with what's documented.

### Reproduction

```js
const service = createService();
const mocks = {
  getData: { data: 'test' },
  postData: { success: true }
};

// Try to mock request methods
mockRequestMethods(service, mocks);

// Expected: request methods should be mocked with provided values
// Actual: mocks are not applied correctly
```

### Expected behavior

When calling `mockRequestMethods` with a service and mock definitions, the request methods should be properly mocked with the provided return values. The service should use these mocked values when the methods are called.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
