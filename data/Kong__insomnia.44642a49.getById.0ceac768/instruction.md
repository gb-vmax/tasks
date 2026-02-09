# Bug Report

### Describe the bug

I'm experiencing a syntax error when trying to use template tags in my requests. The templating system seems to be broken and I'm getting errors about invalid syntax in the extensions module.

### Reproduction

```js
// Try to use any template tag that accesses request data
{% request 'id', 'some-request-id' %}

// Or use the util.models.request.getById function
const request = await context.util.models.request.getById('some-id');
```

When I try to render templates that reference request data, I get errors indicating there's a problem with the template extension code itself. This affects all request-related template tags.

### Expected behavior

Template tags should work normally and be able to fetch request data without throwing syntax errors. The `util.models.request.getById` function should be callable and return request objects as expected.

### System Info

- Insomnia version: latest
- OS: macOS

This seems to have started recently - templates were working fine before. It looks like there might be an issue with how the request utility functions are defined in the templating extensions.

---
Repository: /testbed
