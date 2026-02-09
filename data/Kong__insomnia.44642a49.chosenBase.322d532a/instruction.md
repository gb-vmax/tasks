# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with duplicate cookie handling in workspaces. When multiple cookies with the same domain, path, and key exist in a cookie jar, they're not being properly deduplicated. This results in duplicate cookies being stored and sent with requests.

### Reproduction

1. Create a workspace with a cookie jar
2. Add multiple cookies that have identical domain, path, and key properties but different values
3. The duplicate cookies persist instead of being merged/deduplicated

For example:
```js
// Cookie 1
{ domain: 'example.com', path: '/', key: 'session', value: 'old' }

// Cookie 2  
{ domain: 'example.com', path: '/', key: 'session', value: 'new' }

// Both cookies remain in the jar instead of being merged
```

### Expected behavior

Cookies with the same domain, path, and key should be treated as duplicates (semantically the same cookie), and only one should be kept in the cookie jar. The newer cookie should replace the older one, similar to how browsers handle cookie updates.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues with authentication flows where cookies are being updated, as the old values are persisting alongside the new ones.

---
Repository: /testbed
