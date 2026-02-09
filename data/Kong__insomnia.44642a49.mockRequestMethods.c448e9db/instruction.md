# Bug Report

### Describe the bug

I'm experiencing an issue with the automock functionality where request methods are not being mocked properly. When I try to mock request-type methods on a service, it seems like the mocking is being applied to the wrong method type.

### Reproduction

```js
const mockService = {
  getUserData: async (userId) => {
    // This is a request method that should be mockable
    return fetch(`/api/users/${userId}`);
  }
};

// Attempting to mock request methods
const mockedService = mockRequestMethods(mockService, {
  getUserData: { data: { id: 1, name: 'Test User' } }
});

// The mock doesn't seem to be applied correctly
const result = await mockedService.getUserData(1);
// Expected: { id: 1, name: 'Test User' }
// Actual: Makes real network request instead of using mock
```

### Expected behavior

When using `mockRequestMethods()`, it should properly mock methods that make requests. The mocked methods should return the provided mock data instead of making actual network calls.

### Additional context

This seems to have broken recently. The mocking system appears to be targeting the wrong method type, causing request methods to not be intercepted properly. This is affecting our ability to test services that make API calls.

---
Repository: /testbed
