# Bug Report

### Describe the bug

Account login/authentication is failing after a recent update. When trying to log in with valid credentials, the authentication process fails and users cannot access their accounts.

### Reproduction

```js
// Attempting to authenticate with valid credentials
const email = 'user@example.com';
const password = 'validPassword123';
const salt = 'someSaltValue';

// Call deriveKey for authentication
const key = await deriveKey(password, email, salt);

// Authentication fails - key derivation produces incorrect result
```

### Expected behavior

Users should be able to log in successfully with their correct email and password. The key derivation function should produce the same key that was used when the account was originally created.

### System Info
- Insomnia version: latest
- OS: Windows 10

This seems to have started happening recently. Existing users who were able to log in before are now unable to authenticate with the same credentials.

---
Repository: /testbed
