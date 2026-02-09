# Bug Report

### Describe the bug

I'm experiencing an issue with account authentication after a recent update. When trying to log in with valid credentials, the authentication fails even though the email and password are correct. This seems to be related to how the encryption key is being derived.

### Reproduction

```js
// Try to authenticate with valid credentials
const email = 'user@example.com';
const password = 'correctPassword';
const salt = 'someSalt';

// Derive key for authentication
const key = await deriveKey(password, email, salt);

// Authentication fails with the derived key
// Even though the credentials are correct
```

### Expected behavior

Authentication should succeed when using valid credentials. The key derivation should consistently produce the same key for the same inputs (password, email, salt).

### Additional context

This started happening recently and affects the ability to log in to existing accounts. It seems like the key derivation process might be using the wrong parameters, causing a mismatch between the key used during account creation and the key used during login.

---
Repository: /testbed
