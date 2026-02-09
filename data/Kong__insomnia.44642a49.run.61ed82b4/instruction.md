# Bug Report

### Describe the bug

I'm experiencing an issue with the OS template tag where it's no longer working after a recent update. When trying to use the tag to get system information like CPU details or architecture, nothing is returned and the template just shows as empty.

### Reproduction

Try using the OS template tag in a request:

```
{% os 'arch' %}
```

or

```
{% os 'cpus', 'filter.path' %}
```

The template doesn't render anything. Previously this would return the architecture string or CPU information.

### Expected behavior

The OS template tag should return system information. For example:
- `{% os 'arch' %}` should return something like `x64` or `arm64`
- `{% os 'cpus' %}` should return CPU information as JSON
- When using a filter parameter, it should extract the specified path from the result

### System Info
- Insomnia version: latest
- OS: macOS

This was working fine before, not sure what changed but it seems like the template tag is completely broken now.

---
Repository: /testbed
