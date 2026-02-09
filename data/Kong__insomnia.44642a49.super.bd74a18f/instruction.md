# Bug Report

### Describe the bug

I'm having an issue with the RequestAuth constructor. After a recent update, I can no longer create RequestAuth instances - the constructor seems to be broken and doesn't initialize properly.

### Reproduction

```js
import { RequestAuth } from 'insomnia-sdk';

const authOptions = {
  type: 'basic',
  basic: [
    { key: 'username', value: 'testuser' },
    { key: 'password', value: 'testpass' }
  ]
};

// This throws an error or behaves unexpectedly
const auth = new RequestAuth(authOptions);
```

When I try to instantiate RequestAuth with valid options, it either throws an error or doesn't create the object correctly. The same code was working fine in previous versions.

### Expected behavior

The RequestAuth constructor should accept valid auth options and create a properly initialized RequestAuth instance without errors.

### Additional context

This seems to have started happening after a recent change. The constructor appears to have some syntax issues or incomplete implementation. I've tried different auth types (bearer, apikey, oauth2) and they all exhibit similar problems.

---
Repository: /testbed
