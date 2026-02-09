# Bug Report

### Describe the bug

The `no_proxy` wildcard matching is not working correctly for subdomain patterns. When I configure a wildcard pattern like `*.example.com` in the no_proxy settings, it's not matching URLs as expected.

### Reproduction

Set up no_proxy with a wildcard pattern:
```
no_proxy: *.example.com
```

Try to access:
- `https://api.example.com` - should bypass proxy but doesn't
- `https://subdomain.example.com` - should bypass proxy but doesn't

The wildcard pattern matching seems to be broken. I expected these URLs to match the `*.example.com` pattern and bypass the proxy, but they're still being routed through the proxy.

### Expected behavior

When `*.example.com` is configured in no_proxy:
- Any subdomain under `example.com` should match and bypass the proxy
- `api.example.com`, `test.example.com`, etc. should all bypass the proxy

### Additional context

This seems to have started recently. The wildcard matching used to work fine but now it's not recognizing the pattern correctly. Not sure if this is related to a recent update or configuration change.

---
Repository: /testbed
