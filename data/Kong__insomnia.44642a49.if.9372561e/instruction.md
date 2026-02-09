# Bug Report

### Describe the bug

I'm experiencing an issue with authentication configuration where setting auth options using `VariableList` objects doesn't work as expected. When I pass a `VariableList` to configure authentication, the auth parameters are not being applied to my requests.

### Reproduction

```js
const authParams = new VariableList();
authParams.add({ key: 'username', value: 'myuser' });
authParams.add({ key: 'password', value: 'mypass' });

// Configure auth with VariableList
request.auth.basic(authParams);

// The auth parameters are not being set on the request
// Request goes out without authentication headers
```

### Expected behavior

When passing a `VariableList` object to auth methods, the variables in the list should be properly converted and applied to the request authentication. The request should include the appropriate authentication headers/parameters based on the variables provided.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
