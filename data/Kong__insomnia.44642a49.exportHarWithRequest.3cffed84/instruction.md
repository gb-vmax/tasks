# Bug Report

### Describe the bug

Getting an error when trying to export a request to HAR format. The error message says `Failed to export request` but it's actually failing during the rendering phase, not the export phase. The error seems to reference an undefined variable.

### Reproduction

```js
// Try to export a request with template variables
const request = {
  name: 'Test Request',
  url: '{{ base_url }}/api/test',
  method: 'GET'
}

// This throws an error about renderResult not being defined
await exportHarWithRequest(request, environmentId)
```

### Expected behavior

The request should be rendered first, then exported to HAR format. If rendering fails, it should show a proper error message indicating the rendering failure.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
