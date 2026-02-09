# Bug Report

### Describe the bug

I'm unable to decrypt my synced data after updating to the latest version. When trying to sync my workspace, I get decryption errors and can't access any of my previously synced collections.

### Reproduction

1. Set up account sync with email and password
2. Sync some data to the cloud
3. Update to the latest version
4. Try to sync/decrypt the data
5. Decryption fails with authentication errors

### Expected behavior

The decryption should work correctly with the same email and password combination that was used to encrypt the data originally. Previously synced data should remain accessible after updating.

### Additional context

This seems to have started happening after a recent update. The encryption was working fine before, and I haven't changed my credentials. It looks like there might be an issue with how the encryption key is being derived from the email and password.

---
Repository: /testbed
