# Bug Report

### Duplicate variable declaration causing GitHub OAuth to fail

I'm encountering an issue with the GitHub OAuth flow where the authorization URL generation is broken. When trying to authenticate with GitHub, the application crashes or behaves unexpectedly.

### Reproduction
```js
import { generateAuthorizationUrl } from './github-oauth-provider';

// Attempting to generate authorization URL
const url = generateAuthorizationUrl();
console.log(url);
```

### Expected behavior
The function should successfully generate a valid GitHub OAuth authorization URL with the proper state parameter and scopes.

### Actual behavior
The code fails to execute properly due to what appears to be a variable naming conflict in the module. The `statesCache` variable seems to be declared twice with different types (Set vs Map), which would cause the application to either crash or use the wrong data structure.

### System Info
- Insomnia version: latest
- Node version: 18.x

This is blocking our GitHub integration workflow. Any help would be appreciated!

---
Repository: /testbed
