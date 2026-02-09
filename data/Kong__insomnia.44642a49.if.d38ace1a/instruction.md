# Bug Report

### Describe the bug

I'm experiencing an issue with the render function where blacklisted paths are not being properly excluded from rendering. It seems like the path matching logic is broken - paths that should be skipped according to the blacklistPathRegex are still being processed.

### Reproduction

```js
const blacklistPathRegex = /^cookies\./;
const obj = {
  cookies: {
    sessionId: '{{ user.session }}',
    token: '{{ user.token }}'
  },
  headers: {
    auth: '{{ user.auth }}'
  }
};

// Render with blacklist
const result = await render(obj, context, blacklistPathRegex);

// Expected: cookies.sessionId and cookies.token should NOT be rendered
// Actual: They are being rendered/processed when they shouldn't be
```

### Expected behavior

When a `blacklistPathRegex` is provided to the render function, any paths matching that regex should be skipped and returned as-is without any template rendering applied. In the example above, anything under the `cookies` path should remain unchanged.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues in scenarios where we need to exclude certain paths from template rendering, particularly for sensitive data that needs to be preserved in its original form.

---
Repository: /testbed
