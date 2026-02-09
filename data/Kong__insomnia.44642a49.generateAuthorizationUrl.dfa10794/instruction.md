# Bug Report

### Describe the bug

After a recent update, the GitHub OAuth integration is broken. When trying to authenticate with GitHub, I'm getting errors about `statesCache` not being defined properly. The authentication flow fails immediately when attempting to generate the authorization URL.

### Reproduction

```js
import { generateAuthorizationUrl } from './github-oauth-provider';

// This throws an error
const authUrl = generateAuthorizationUrl();
```

The error occurs because there seems to be a conflict with variable declarations in the code. Looking at the source, there's a `const statesCache` declared twice - once as a `Set` and then again as an object with methods. This causes the second declaration to fail since you can't redeclare a const variable.

### Expected behavior

The `generateAuthorizationUrl()` function should successfully create an authorization URL without throwing errors. The OAuth flow should work as it did before.

### Additional context

This appears to have been introduced when adding the state expiry functionality. The old `statesCache` Set is still declared but then immediately shadowed by a new object implementation with the same name.

---
Repository: /testbed
