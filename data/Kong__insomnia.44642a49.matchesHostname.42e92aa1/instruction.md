# Bug Report

### Describe the bug

The no_proxy rule matching isn't working correctly for hostnames that start with `*.` wildcard patterns. When I configure a no_proxy rule like `*.example.com`, it's not matching subdomains as expected.

### Reproduction

When setting up proxy bypass rules with wildcard patterns:

```js
// no_proxy configuration
const noProxyRule = '*.example.com';

// These should match but don't:
// - subdomain.example.com
// - api.example.com
// - any-subdomain.example.com
```

The pattern `*.example.com` should match any subdomain of `example.com`, but the current implementation doesn't handle this correctly. It seems like the wildcard at the beginning is being processed incorrectly.

### Expected behavior

When a no_proxy rule contains `*.domain.com`, it should match all subdomains like:
- `api.domain.com`
- `test.domain.com`
- `subdomain.domain.com`

But it should NOT match:
- `domain.com` itself (no subdomain)
- `notdomain.com`

### Additional context

This is affecting proxy configuration where we need to bypass the proxy for internal subdomains but still use the proxy for the main domain. The `.*.` prefix pattern works, but `*.` at the start doesn't behave as expected.

---
Repository: /testbed
