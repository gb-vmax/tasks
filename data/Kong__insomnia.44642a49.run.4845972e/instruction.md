# Bug Report

### Describe the bug

After a recent update, the faker template tag is no longer working correctly. When I try to use it in my requests, I'm getting errors about the function not being callable or returning undefined values.

### Reproduction

When using the faker template tag with a simple function like this:

```
{% faker 'firstName' %}
```

The template doesn't render correctly and instead of getting a fake first name, I'm seeing unexpected behavior. It seems like the function is being called incorrectly or the return value is being processed in a way that breaks the output.

I also noticed that if I try to use it with any parameters, things get even more broken. The faker functions that used to work fine are now failing silently or returning null/undefined.

### Expected behavior

The faker template tag should call the underlying faker function and return the generated value as it did before. Simple faker calls like `{% faker 'firstName' %}` should work without any issues.

### System Info
- Insomnia version: latest
- OS: macOS

This was working fine in the previous version, so it seems like a regression introduced in the recent changes to the template tag system.

---
Repository: /testbed
