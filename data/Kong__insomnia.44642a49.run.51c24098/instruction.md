# Bug Report

### Describe the bug

The UUID template tag appears to be broken after a recent change. When trying to use it in templates, I'm getting syntax errors and the tag doesn't generate UUIDs anymore.

### Reproduction

```js
// Using the UUID template tag in a request
{% uuid 'v4' %}

// Or with v1
{% uuid 'v1' %}
```

When I try to use these tags, they fail to execute properly. The template rendering seems to break completely.

### Expected behavior

The UUID tag should generate valid UUIDs:
- `{% uuid 'v4' %}` should generate a v4 UUID like `550e8400-e29b-41d4-a716-446655440000`
- `{% uuid 'v1' %}` should generate a v1 UUID

### Additional context

This was working fine before, but now it seems like something got corrupted in the template tag implementation. The code looks incomplete or cut off somehow.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
