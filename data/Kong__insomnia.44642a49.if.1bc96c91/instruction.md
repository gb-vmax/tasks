# Bug Report

### Describe the bug

I'm experiencing an issue where response bodies are not being loaded correctly. When I make a request that should return content, I'm getting an empty response instead of the actual data.

### Reproduction

```js
// Make a request that returns a response with a body
const response = await sendRequest({
  url: 'https://api.example.com/data',
  method: 'GET'
});

// Expected: response body contains the API data
// Actual: response body is empty (0 bytes)
```

The issue occurs when:
1. Send any request that returns a response body
2. Try to view the response content
3. The response appears empty even though the server returned data

### Expected behavior

When a response has a body stored at a valid `bodyPath`, the content should be read from that file and returned. Currently it seems like responses with valid body paths are being treated as if they have no body, resulting in empty buffers being returned instead of the actual response content.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
