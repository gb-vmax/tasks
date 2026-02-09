# Bug Report

### Describe the bug

After a recent update, request names are not being displayed correctly in the UI. The names appear to be cached or frozen, and changes to environment variables that should affect the request name are not reflected.

### Reproduction

```js
// Set up a request with a dynamic name
const request = {
  name: 'Request for ${env_name}'
}

// Initial environment
const context = {
  env_name: 'production'
}

// Get the name - shows "Request for production"
request.getName()

// Update the environment variable
context.env_name = 'staging'

// Get the name again - still shows "Request for production" instead of "Request for staging"
request.getName()
```

### Expected behavior

The request name should update dynamically when environment variables change. If the name contains variable placeholders like `${variable_name}`, they should be interpolated with the current values from the context each time `getName()` is called.

### Additional context

This seems to have started happening recently. Previously, request names would update properly when switching environments or modifying environment variables. Now the names seem to be stuck with their initial values.

The issue is particularly noticeable when:
1. Switching between different environments
2. Modifying environment variables that are used in request names
3. Working with multiple requests that use the same variable names

---
Repository: /testbed
