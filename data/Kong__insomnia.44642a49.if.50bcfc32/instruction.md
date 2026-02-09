# Bug Report

### Describe the bug

I'm encountering a syntax error in the authentication module that prevents the code from running. It looks like there's some malformed code in the OAuth2 authentication handling section - specifically in the `findValueInOauth2Options` function area.

### Reproduction

When trying to use OAuth2 authentication with requests, the application fails to load/compile. The error occurs in the `auth.ts` file in the `fromPreRequestAuth` function.

```js
// Attempting to configure OAuth2 auth
const auth = {
  type: 'oauth2',
  oauth2: [
    { key: 'accessToken', value: 'my-token' },
    { key: 'addTokenTo', value: 'header' }
  ]
};

// Application fails to start due to syntax error
```

### Expected behavior

The OAuth2 authentication should be properly parsed and applied to requests without any compilation/syntax errors. The code should execute cleanly when processing OAuth2 authentication options.

### Additional context

This appears to be related to the OAuth2 value transformation logic. The code structure seems broken - there are duplicate function definitions and the logic flow doesn't look right. It seems like code got duplicated or improperly merged during a recent change.

---
Repository: /testbed
