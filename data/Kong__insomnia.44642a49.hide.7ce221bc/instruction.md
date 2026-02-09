# Bug Report

### Describe the bug

I'm experiencing an issue with the response template tag where the "Filter (JSONPath or XPath)" field is showing up when it shouldn't be visible. Specifically, the filter input appears even when certain attributes are selected that don't support filtering.

### Reproduction

Steps to reproduce:
1. Add a response template tag to a request
2. Select an attribute like "status" or "status-message" 
3. Notice that the base64 encoding filter field is still visible

The filter field should be hidden for attributes that don't support filtering (like `raw`, `url`, `status`, and `status-message`), but it's currently showing up regardless of which attribute is selected.

Additionally, when no request is selected in the second argument, the filter field still appears when it should be hidden.

### Expected behavior

The base64 encoding filter field should only be visible for attributes that actually support filtering (like `body`, headers, etc.). It should be hidden when:
- Attributes like `raw`, `url`, `status`, or `status-message` are selected
- No request is selected

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
