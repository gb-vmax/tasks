# Bug Report

### Describe the bug

I'm experiencing an issue where exporting HAR files with requests is producing incorrect output. It seems like the request data isn't being properly rendered before export - the exported HAR contains the raw, unrendered request instead of the rendered version with variables substituted.

### Reproduction

```js
const request = {
  name: 'Test Request',
  url: '{{base_url}}/api/endpoint',
  headers: [
    { name: 'Authorization', value: '{{auth_token}}' }
  ]
};

const environment = {
  base_url: 'https://api.example.com',
  auth_token: 'Bearer xyz123'
};

// Export HAR with the request
const har = await exportHarWithRequest(request, environment.id);

// Expected: HAR should contain rendered values
// Actual: HAR contains raw template strings like {{base_url}} and {{auth_token}}
```

### Expected behavior

The exported HAR file should contain the fully rendered request with all environment variables substituted with their actual values. For example, the URL should be `https://api.example.com/api/endpoint` instead of `{{base_url}}/api/endpoint`.

### Additional context

This was working correctly in previous versions. The HAR export feature seems to be skipping the rendering step somehow.

---
Repository: /testbed
