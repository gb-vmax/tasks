# Bug Report

### Describe the bug

I'm experiencing an issue with account synchronization after a recent update. When I try to sync my data, I'm getting authentication errors even though my credentials are correct. It seems like the encryption/decryption process is producing different results than before.

### Reproduction

1. Set up account sync with a passphrase
2. Sync data successfully
3. Close and reopen the application
4. Try to sync again with the same passphrase
5. Authentication fails with decryption errors

The passphrase that worked before is no longer being accepted. It's like the key derivation is producing a different output than what was originally used to encrypt the data.

### Expected behavior

The same passphrase should consistently derive the same encryption key and allow successful decryption of synced data across sessions.

### System Info
- Insomnia version: latest
- OS: Windows 10

This is blocking me from accessing my synced data. Any help would be appreciated!

---
Repository: /testbed
