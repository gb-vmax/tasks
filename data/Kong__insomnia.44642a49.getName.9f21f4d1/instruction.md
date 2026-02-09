# Bug Report

### Describe the bug

After a recent update, the `getName()` method in the request context is throwing syntax errors. It looks like there's a problem with the function definition - the code won't even parse.

### Reproduction

```js
const request = context.request;

// This throws a syntax error
const name = request.getName();
```

When trying to use the plugin API with `request.getName()`, I'm getting parse/syntax errors and the plugin fails to load entirely.

### Expected behavior

The `getName()` method should return the request name as it did before. The basic usage `request.getName()` should work without any syntax errors.

### Additional context

This seems to have broken after the latest changes to the request context. The method was working fine in the previous version. It looks like something went wrong with how the function is defined in the source code.

---
Repository: /testbed
