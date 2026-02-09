# Bug Report

### Describe the bug

I'm having an issue with the `mockRequestMethods` function in the automock module. When I try to mock request methods for a service, it seems like the mocking is being applied to the wrong method type. The mocked behavior isn't being applied to my request methods as expected.

### Reproduction

```js
const service = {
  getUserData: async () => { /* request implementation */ }
};

const mocks = {
  getUserData: { data: 'mocked response' }
};

// Try to mock request methods
mockRequestMethods(service, mocks);

// The request method doesn't use the mock
const result = await service.getUserData();
// Expected: mocked response
// Actual: original implementation runs
```

### Expected behavior

When calling `mockRequestMethods`, the request methods should be mocked with the provided mock data. The function should apply mocks to `MethodType.request` methods, not response methods.

### Additional context

This seems to have started recently. I'm using the automock functionality to test my IPC handlers and the request method mocking just stopped working properly.

---
Repository: /testbed
