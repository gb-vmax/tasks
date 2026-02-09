# Bug Report

### Describe the bug

The UUID template tag is not working correctly after a recent update. When I try to generate UUIDs in my templates, I'm getting errors about invalid parameters even though I'm using the basic v4 UUID generation without any extra arguments.

### Reproduction

```js
// This used to work but now throws an error
{% uuid 'v4' %}

// Even the default case seems broken
{% uuid %}
```

The template rendering fails and I see errors in the console about unexpected parameters or function calls.

### Expected behavior

The UUID template tag should generate valid UUIDs like it did before:
- `{% uuid %}` should generate a v4 UUID by default
- `{% uuid 'v4' %}` should generate a v4 UUID
- `{% uuid 'v1' %}` should generate a v1 UUID

All of these should return a standard formatted UUID string without any errors.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening after the recent template tag updates. The UUID generation was working fine in the previous version.

---
Repository: /testbed
