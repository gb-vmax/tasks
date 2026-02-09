# Bug Report

### Describe the bug

The JSONPath Filter option is now hidden for OS template tag functions that return primitive values like strings and numbers. This breaks existing templates that were using JSONPath filtering with functions like `homedir`, `tmpdir`, `platform`, `arch`, etc.

### Reproduction

```js
// Using the OS template tag with a function that returns a string
{% os 'homedir', 'filter', '$.someProperty' %}

// The JSONPath filter field is now hidden in the UI
// Previously this was available even though it might not be needed
```

Steps to reproduce:
1. Open a request that uses the OS template tag
2. Select a function like `homedir`, `platform`, or `arch`
3. Notice that the JSONPath Filter input field is no longer visible in the UI
4. Existing templates using these functions with filters stop working

### Expected behavior

The JSONPath Filter field should remain visible for all OS functions, or at minimum for functions that could potentially benefit from it. Users should be able to configure the filter even if the return value is a primitive type (the filter would just pass through the value unchanged).

This is causing issues with existing templates that may have been using filters with these functions.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
