# Bug Report

### Describe the bug

When importing Swagger 2.0 specs, the generated example values for email parameters are malformed. The email addresses are missing the dot (`.`) between the domain and TLD, resulting in invalid email formats like `user@examplecom` instead of `user@example.com`.

### Reproduction

```js
// Import a Swagger 2.0 spec with an email parameter
const spec = {
  swagger: '2.0',
  paths: {
    '/users': {
      post: {
        parameters: [{
          name: 'email',
          in: 'body',
          type: 'string',
          format: 'email'
        }]
      }
    }
  }
}

// After import, the generated example email is malformed
// Expected: something like "abc12@def45.com"
// Actual: something like "abc12@def45com" (missing dot before TLD)
```

### Expected behavior

Generated email examples should be valid email addresses with proper formatting, including a dot separator between the domain name and top-level domain (e.g., `user@domain.com`, `test@example.org`).

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
