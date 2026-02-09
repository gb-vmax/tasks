# Bug Report

Title: `ok()` function throwing errors intermittently in remark-directive

I'm experiencing a strange issue where the `ok()` validation function in the remark-directive vendor bundle is throwing errors inconsistently. It seems to work fine on the first call, but then fails on the second call, then works again on the third, and so on.

### Steps to reproduce:
1. Use remark-directive in a project
2. Call any functionality that internally uses the `ok()` validation function multiple times
3. Every other call throws "Validation failed" error

### Expected behavior
The `ok()` function should consistently validate without throwing errors, or at least behave predictably across all calls.

### Actual behavior
The function throws `Error: Validation failed` on every second invocation, making it impossible to reliably use features that depend on this validation.

Example of what I'm seeing:
```
First call: works fine
Second call: Error: Validation failed
Third call: works fine  
Fourth call: Error: Validation failed
...
```

This is blocking my ability to parse markdown with directives reliably. Has anyone else encountered this? It feels like there might be some state being tracked incorrectly.

---
Repository: /testbed
