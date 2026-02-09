# Bug Report

### Describe the bug

The redirect validation is throwing errors even when the redirect configuration is valid. Every redirect now fails with a validation error message, even for correctly formatted redirects that were working before.

### Reproduction

```js
const redirect = {
  from: '/old-page',
  to: '/new-page'
};

// This valid redirect now throws an error
validateRedirect(redirect);
// Error: {"from":"/old-page","to":"/new-page"} => Validation error: undefined
```

### Expected behavior

Valid redirects should pass validation without throwing errors. Only invalid redirects should trigger validation errors.

### Additional context

This seems to have broken all redirect functionality in the plugin. Even basic redirects that follow the documented format are being rejected.

---
Repository: /testbed
