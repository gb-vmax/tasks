# Bug Report

### Describe the bug

I'm experiencing issues with account synchronization after a recent update. When trying to sync my workspace data, I'm getting authentication failures and the encrypted data appears to be corrupted or invalid.

### Reproduction

Steps to reproduce:
1. Set up account sync with a passphrase
2. Encrypt some workspace data
3. Try to decrypt the data on another device or after logging out/in
4. Decryption fails with invalid key errors

The encrypted data format seems to have changed and previously encrypted content can no longer be decrypted properly. This is blocking my ability to sync across devices.

### Expected behavior

The encryption/decryption should work consistently and encrypted data should be decryptable using the same passphrase that was used to encrypt it. Cross-device sync should work without authentication errors.

### System Info
- Insomnia version: latest
- OS: macOS
- Using account sync: Yes

This is pretty critical as it's preventing me from accessing my synced workspaces. Any help would be appreciated!

---
Repository: /testbed
