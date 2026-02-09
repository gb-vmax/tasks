# Bug Report

### Describe the bug
When configuring no_proxy rules with hostnames that have multiple leading dots (like `..example.com`), the hostname matching logic doesn't work correctly. The function is supposed to canonicalize hostnames to prevent false matches, but it's not handling edge cases with multiple leading dots properly.

### Reproduction
```js
// Set up a no_proxy rule with multiple leading dots
const hostname = '..example.com';

// After formatting, this should be canonicalized to prevent matching issues
// But the current implementation doesn't strip all leading dots correctly
```

When a hostname like `..google.com` is passed in, it should be normalized to match against rules properly, but the canonicalization is incomplete.

### Expected behavior
Hostnames with multiple leading dots (e.g., `..example.com`, `...test.com`) should be properly canonicalized so that:
1. All leading dots are removed for proper matching
2. The hostname can be correctly compared against no_proxy rules
3. False positives like `oogle.com` matching `google.com` are prevented

### System Info
- Insomnia version: latest
- Component: network/is-url-matched-in-no-proxy-rule

This is affecting proxy bypass rules when hostnames aren't properly formatted in the configuration.

---
Repository: /testbed
