# Bug Report

### Describe the bug

I'm encountering an issue with the prompt template tag where titles with special characters are being rejected. After a recent update, I can no longer use certain characters in my prompt titles that were previously working fine.

### Reproduction

When trying to create a prompt with a title that contains special characters, the validation fails:

```js
// This used to work but now fails validation
prompt('user@email', 'Enter email')

// This also fails
prompt('api.key', 'Enter API key')

// Even this fails
prompt('config/path', 'Enter config path')
```

All of these examples now show an error message saying the title can only contain letters, numbers, spaces, hyphens, and underscores.

### Expected behavior

The prompt should accept titles with special characters like `@`, `.`, `/`, etc. These characters are commonly used in identifiers and were working before. The validation seems too restrictive now.

### Additional context

This is breaking existing templates that rely on these naming conventions. Many users use email-like identifiers or path-like structures for their prompt titles.

---
Repository: /testbed
