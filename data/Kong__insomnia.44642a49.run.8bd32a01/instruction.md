# Bug Report

### Describe the bug

After a recent update, the faker template tag is throwing errors when I try to use it without providing additional arguments. It seems like the function signature changed but it's breaking existing templates that were working fine before.

### Reproduction

```js
// This used to work but now throws an error
{% faker 'name.firstName' %}

// The template tag expects additional parameters now
// but I just want to use the basic faker function without args
```

### Steps to reproduce:
1. Create a template using the faker tag with just the function name
2. Try to render the template
3. Get an error about missing or invalid arguments

### Expected behavior

The faker template tag should work with just the function name parameter like it did before. Optional parameters for arguments and seed should not break existing usage when they're not provided.

### System Info
- Insomnia version: latest
- OS: macOS

This is affecting all my existing API templates that use faker functions. Would appreciate a fix or guidance on how to update my templates!

---
Repository: /testbed
