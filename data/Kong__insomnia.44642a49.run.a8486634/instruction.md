# Bug Report

### Describe the bug

When using the OS template tag, the system crashes or returns incomplete results. It appears that template rendering is broken after a recent change to the OS template tag functionality.

### Reproduction

```js
// Using the OS template tag with any function
{% os 'arch' %}

// Or with filters
{% os 'cpus', '$.model' %}
```

The template fails to render and may cause the application to hang or crash.

### Expected behavior

The OS template tag should properly return system information like architecture or CPU details. When using filters, it should apply JSONPath queries and return formatted results.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
