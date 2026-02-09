# Bug Report

### Describe the bug
After a recent update, HTTP responses with multiple redirects are not being parsed correctly. The response headers appear to be empty or missing when there are redirect chains involved.

### Reproduction
```js
// Make a request that involves redirects (e.g., 301 -> 302 -> 200)
const response = await sendRequest({
  url: 'https://example.com/redirect-chain',
  followRedirects: true
});

// Expected: response should contain headers from all redirects
// Actual: headers array is empty or missing redirect information
console.log(response.headers); // Returns empty or incomplete data
```

### Expected behavior
When a request goes through multiple redirects, all redirect responses should be properly parsed and their headers should be available. Each redirect in the chain should have its status code, version, and headers preserved.

### System Info
- Insomnia version: latest
- OS: Various

This seems to have started after the recent changes to the header parsing logic. Requests without redirects work fine, but multi-redirect scenarios fail to parse properly.

---
Repository: /testbed
