# Bug Report

### Describe the bug

I'm experiencing an issue with the no_proxy rule matching functionality. When I try to use a no_proxy rule with an IPv6 address, it's not being matched correctly and the proxy is still being applied even though it shouldn't be.

### Reproduction

```js
// Setting no_proxy with an IPv6 address
process.env.no_proxy = '[::1]:8080'

// Making a request to localhost IPv6
// Expected: Direct connection (no proxy)
// Actual: Proxy is still being used
```

The issue seems to occur specifically when using IPv6 addresses in square bracket notation (like `[::1]` or `[2001:db8::1]`). Regular hostnames with ports work fine, but IPv6 addresses are not being parsed correctly.

### Expected behavior

When an IPv6 address is specified in the no_proxy rules (e.g., `[::1]:8080` or `[2001:db8::1]`), requests to that address should bypass the proxy. The colon characters within the IPv6 address should not interfere with the port parsing.

### Additional context

This appears to be related to how the no_proxy zone parsing handles colons. IPv6 addresses contain multiple colons (e.g., `::1` has colons that are part of the address itself), which might be causing confusion with port delimiter parsing.

---
Repository: /testbed
