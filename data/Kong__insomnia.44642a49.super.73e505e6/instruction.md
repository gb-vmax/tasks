# Bug Report

### Describe the bug

After a recent update, the `RequestAuth` constructor appears to be broken. When trying to create a new `RequestAuth` instance, the code doesn't seem to execute properly. The constructor validation logic that checks for valid auth types is no longer working as expected.

### Reproduction

```js
import { RequestAuth } from '@insomnia/sdk';

// This should create a basic auth instance
const auth = new RequestAuth({
  type: 'basic',
  basic: [
    { key: 'username', value: 'testuser' },
    { key: 'password', value: 'testpass' }
  ]
});

// Constructor doesn't complete properly
console.log(auth); // undefined or incomplete object
```

### Expected behavior

The `RequestAuth` constructor should properly initialize the auth object and validate the auth type. It should throw an error for invalid types and successfully create the auth instance for valid types like 'basic', 'bearer', 'apikey', etc.

### Additional context

This seems to have broken after some recent changes to the auth module. The constructor logic appears incomplete - it looks like there's a method definition inside the constructor which doesn't make sense. The parent class initialization with `super()` and the type validation should complete before any other logic runs.

---
Repository: /testbed
