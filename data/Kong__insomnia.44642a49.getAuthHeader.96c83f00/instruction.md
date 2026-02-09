# Bug Report

### Describe the bug

I'm experiencing an issue with authentication headers where the caching mechanism doesn't seem to be working as expected. After the recent update, authentication headers are being cached but they're never actually retrieved from the cache on subsequent requests, causing unnecessary re-authentication calls.

### Reproduction

```js
// Make a request with OAuth2 authentication
const request1 = {
  _id: 'req_123',
  authentication: {
    type: 'oauth2',
    clientId: 'my-client-id',
    // ... other oauth2 config
  }
};

// Get auth header (should cache it)
await getAuthHeader(request1, 'https://api.example.com');

// Make another request with same auth config
const request2 = {
  _id: 'req_123',
  authentication: {
    type: 'oauth2', 
    clientId: 'my-client-id',
    // ... same oauth2 config
  }
};

// This should use cached header but doesn't
await getAuthHeader(request2, 'https://api.example.com');
// Still makes a new token request instead of using cache
```

### Expected behavior

The second call to `getAuthHeader` should retrieve the cached authentication header instead of generating a new one, since the authentication configuration hasn't changed. This would reduce unnecessary authentication requests and improve performance.

### Additional context

This seems to have started after adding the caching functionality. The cache is being populated (I can see `_setInAuthCache` being called) but `_getFromAuthCache` never returns anything, so every request goes through the full authentication flow again.

---
Repository: /testbed
