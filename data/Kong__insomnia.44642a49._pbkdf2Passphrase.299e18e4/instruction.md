# Bug Report

### Describe the bug

I'm having issues with account encryption/decryption after a recent update. When I try to sync my data or log in, I'm getting authentication failures and the encrypted data can't be decrypted properly. It seems like the encryption keys being generated are different from what they should be.

### Reproduction

1. Set up account sync with a passphrase
2. Encrypt some data
3. Try to decrypt the data with the same passphrase
4. Decryption fails with invalid key errors

The encrypted data that was working before is now unreadable. It looks like the key derivation is producing different results than expected.

### Expected behavior

The PBKDF2 key derivation should generate consistent encryption keys that can properly encrypt and decrypt data. Using the same passphrase and salt should always produce the same derived key.

### Additional context

This appears to affect both the browser crypto API path and the Forge fallback path. The issue started appearing recently and is blocking account sync functionality.

---
Repository: /testbed
