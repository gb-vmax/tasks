# Bug Report

### Describe the bug

The UUID template tag is generating errors when trying to create v4 UUIDs. When I use the default UUID type or explicitly specify 'v4', I get an error message saying "Invalid UUID type" instead of getting a valid UUID.

### Reproduction

```js
// Using the UUID template tag with default settings (should be v4)
{% uuid %}

// Or explicitly specifying v4
{% uuid 'v4' %}
{% uuid '4' %}
```

Both cases throw an error: `Invalid UUID type "v4"`

### Expected behavior

The UUID template tag should generate a valid v4 UUID by default and when explicitly requesting v4. Only invalid UUID types should throw errors.

### Additional context

- v1 UUIDs seem to work fine (`{% uuid 'v1' %}`)
- This appears to affect both the default behavior and explicit v4 requests
- The error message is confusing because v4 is actually a valid UUID type

---
Repository: /testbed
