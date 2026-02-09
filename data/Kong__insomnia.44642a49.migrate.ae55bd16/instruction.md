# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with cookie jar migration. When loading existing cookie jars that contain duplicate cookies or cookies with various expiration date formats, the application seems to behave unexpectedly.

### Reproduction

I have a cookie jar with the following structure:

```js
{
  cookies: [
    {
      key: 'session',
      domain: 'example.com',
      path: '/',
      expires: '2024-12-31T23:59:59Z',
      creation: new Date('2024-01-01')
    },
    {
      key: 'session',
      domain: 'example.com',
      path: '/',
      expires: 1735689599000,
      creation: new Date('2024-01-02')
    }
  ]
}
```

When this cookie jar is loaded/migrated:
1. Both cookies have the same key, domain, and path (duplicates)
2. The expiration dates are in different formats (string vs timestamp)
3. After migration, I expected to see only one cookie (the most recent one based on creation time)

### Expected behavior

- Duplicate cookies should be deduplicated based on key, domain, and path
- The most recently created cookie should be kept
- Cookie expiration dates should be normalized to a consistent format
- Invalid expiration dates should be handled gracefully

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues when syncing cookie jars across different sessions. Would appreciate any insights on whether this is expected behavior or if there's a workaround.

---
Repository: /testbed
