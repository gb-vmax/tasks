# Bug Report

### Describe the bug

I'm experiencing an issue where template rendering is not working correctly. It seems like all template variables are being rendered even when they should be blacklisted/excluded based on the path regex pattern.

### Reproduction

```js
const template = {
  url: 'https://example.com/{{ secret }}',
  headers: {
    authorization: 'Bearer {{ token }}'
  }
}

const blacklistRegex = /secret|token/

// Expected: secret and token should NOT be rendered
// Actual: Everything gets rendered regardless of blacklist
const result = await render(template, context, { blacklistPathRegex: blacklistRegex })
```

### Expected behavior

When a `blacklistPathRegex` is provided, any paths matching that pattern should be skipped during rendering and left as-is. Instead, it appears the blacklist is being completely ignored and all template variables are being processed.

### Additional context

This is causing sensitive template variables to be rendered when they shouldn't be, which is a security concern in our workflow. The blacklist feature seems to have stopped working entirely.

---
Repository: /testbed
