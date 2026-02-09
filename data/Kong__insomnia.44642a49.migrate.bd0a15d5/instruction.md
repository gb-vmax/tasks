# Bug Report

### Describe the bug

After a recent update, client certificates with wildcard hosts are not matching correctly. When I set up a certificate with a host pattern like `*.example.com`, it's not being applied to requests to subdomains.

### Reproduction

```js
// Create a client certificate with wildcard host
const cert = {
  host: '*.api.example.com',
  cert: 'cert-data',
  key: 'key-data'
}

// The certificate should match requests to:
// - test.api.example.com
// - staging.api.example.com
// etc.

// But it's not being matched properly
```

Also noticing some weird behavior with hosts that have protocols or trailing slashes - they seem to be handled inconsistently now.

### Expected behavior

- Wildcard patterns should work for matching subdomains
- Hosts with `https://` prefix should be handled the same as without
- Trailing slashes shouldn't affect matching
- Default ports (80, 443) should be normalized

### Additional context

This seems to have started after some changes to the certificate model. The certificate configuration UI accepts these formats but they don't work as expected when making requests.

---
Repository: /testbed
