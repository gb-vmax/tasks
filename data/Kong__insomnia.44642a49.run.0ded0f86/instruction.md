# Bug Report

### Describe the bug

The UUID template tag is throwing errors when trying to generate v3 or v5 UUIDs. The function seems to be looking for namespace constants that don't exist on the uuid library.

### Reproduction

Try using the UUID template tag with v3 or v5:

```js
// Attempting to generate a v3 UUID with DNS namespace
{% uuid 'v3', 'dns', 'example.com' %}

// Or with v5
{% uuid 'v5', 'url', 'https://example.com' %}
```

This results in an error because `uuid.v5.DNS` and `uuid.v5.URL` are not valid properties. The uuid library doesn't expose namespace constants this way.

### Expected behavior

Should successfully generate v3/v5 UUIDs using the standard namespace constants. The uuid library provides these as string constants (like `uuid.v5.DNS` should be the actual UUID string for the DNS namespace), not as properties on the version functions.

### Additional context

This is affecting template rendering when trying to use namespace-based UUID generation. The v1 and v4 UUID generation still works fine since they don't require namespaces.

---
Repository: /testbed
