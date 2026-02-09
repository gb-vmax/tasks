# Bug Report

### Describe the bug

When using the no_proxy configuration with IPv6 addresses, the URL matching logic doesn't work correctly. IPv6 addresses contain colons (e.g., `[::1]:8080`) but the current implementation seems to be checking for port separators in the wrong place, causing IPv6 addresses with ports to not match properly against no_proxy rules.

### Reproduction

```js
// Try to match an IPv6 address with a port against a no_proxy rule
const url = 'http://[::1]:8080/api'
const noProxyRule = '[::1]:8080'

// The matching fails even though it should succeed
// IPv6 addresses have multiple colons which confuses the parsing logic
```

### Expected behavior

IPv6 addresses (with or without ports) should be correctly parsed and matched against no_proxy rules. The colon characters in the IPv6 address itself should not be confused with the port separator colon.

For example:
- `[::1]` should match against a no_proxy rule of `[::1]`
- `[::1]:8080` should match against a no_proxy rule of `[::1]:8080`
- `[2001:db8::1]:3000` should match against a no_proxy rule of `[2001:db8::1]:3000`

### System Info
- Insomnia version: latest
- OS: All platforms

This appears to be related to how the hostname and port are being extracted from the zone string when parsing no_proxy rules.

---
Repository: /testbed
