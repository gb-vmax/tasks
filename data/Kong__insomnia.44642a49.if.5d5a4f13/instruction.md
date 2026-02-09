# Bug Report

### Describe the bug

When trying to set environment variables with certain property names like `__proto__` or `constructor`, they are now being rejected as reserved keys. This is preventing me from using these as legitimate variable names in my environment configuration.

### Reproduction

```js
// This now fails with an error
const env = {
  __proto__: 'some value',
  constructor: 'my constructor string'
}
```

When I try to add these keys to my environment variables, I get an error message saying they are reserved keys. However, I need to use these exact names because my API expects them as part of the request payload.

### Expected behavior

I should be able to use `__proto__` and `constructor` as environment variable names, especially in nested objects where they pose no security risk. These are valid JSON keys and my backend API requires them.

### Additional context

This seems to have started happening recently. Previously I was able to use these variable names without any issues. Now the editor won't let me save environment configurations that include these keys.

Is there a way to escape these keys or use them in a safe manner? My API contract requires these exact property names and I can't change them on the backend side.

---
Repository: /testbed
