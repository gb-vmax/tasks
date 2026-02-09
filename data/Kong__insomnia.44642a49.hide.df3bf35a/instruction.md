# Bug Report

### Describe the bug
I'm experiencing an issue with the template tag filter field visibility logic. When working with template tags that have encoding options, the filter field is not showing up in certain cases where it should be visible.

### Reproduction
When using a template tag with:
1. An attribute value that is NOT 'raw' or 'url' (e.g., 'body', 'header', etc.)
2. A valid request ID is present

The filter field should be visible, but it's currently hidden.

Example scenario:
```
- Attribute: 'body'
- Request ID: 'req_123'
- Expected: Filter field visible
- Actual: Filter field hidden
```

It seems like the visibility logic isn't properly checking for the presence of the request ID before deciding whether to hide the filter field.

### Expected behavior
The filter field should be visible when:
- The attribute value is not 'raw' or 'url', AND
- A request ID is available

The filter field should only be hidden when:
- The attribute value is 'raw' or 'url', OR
- No attribute value is provided, OR
- No request ID is available

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
