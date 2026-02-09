# Bug Report

### Describe the bug

I'm experiencing issues when exporting HAR files for requests. The export process seems to hang or take an extremely long time to complete, and sometimes it fails with plugin-related errors. This appears to be happening consistently with certain requests in my workspace.

### Reproduction

```js
// Try to export a HAR file for a request
const request = {
  _id: 'req_123',
  name: 'My API Request',
  url: 'https://api.example.com/endpoint',
  method: 'GET'
};

await exportHarWithRequest(request, environmentId);
// This takes much longer than expected and sometimes fails
```

### Expected behavior

The HAR export should complete quickly (within a reasonable time) and not retry multiple times when there are no transient failures. The export process should be straightforward and not introduce unnecessary delays.

### Additional context

This started happening recently and I noticed that even successful exports are taking significantly longer than they used to. Sometimes I see errors mentioning plugins and retries, which is confusing because my request doesn't have any special plugin configuration.

The delay is particularly noticeable when exporting multiple requests in succession - what used to take a few seconds now takes much longer.

---
Repository: /testbed
