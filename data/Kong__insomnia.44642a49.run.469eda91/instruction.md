# Bug Report

### Describe the bug

After a recent update, the faker template tag is throwing errors when trying to use it without any parameters. The template tag seems to be expecting additional arguments that weren't required before, breaking existing templates that use faker functions without parameters.

### Reproduction

```js
// This used to work but now fails
{% faker 'person.firstName' %}

// Error occurs when trying to generate fake data
// The faker function is being called but something about the parameter handling is broken
```

### Expected behavior

The faker template tag should work without any additional parameters, just like it did before. Calling `{% faker 'person.firstName' %}` should generate a random first name without requiring extra configuration.

### Additional context

This appears to have broken after some changes to how the template tag handles its arguments. The basic use case of generating fake data without parameters should still be supported for backwards compatibility.

---
Repository: /testbed
