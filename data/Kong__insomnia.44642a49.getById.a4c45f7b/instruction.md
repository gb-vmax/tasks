# Bug Report

### Describe the bug

The template tag context's `util.models.request.getById()` function appears to have a syntax error that breaks the entire templating system. When trying to use any plugin template tags that rely on the request model utilities, the application fails to load or execute properly.

### Reproduction

```js
// In a plugin template tag
async run(context) {
  const request = await context.util.models.request.getById('req_123');
  // This should work but the entire context object seems broken
  return request?.name || 'N/A';
}
```

### Expected behavior

The `getById` method should successfully retrieve a request by its ID and return it. Plugin template tags that use `context.util.models.request.getById()` should work without errors.

### Additional context

This seems to have broken recently. The templating extensions are not functioning properly and it looks like there might be a structural issue with how the `getById` method is defined in the type definitions or implementation.

---
Repository: /testbed
