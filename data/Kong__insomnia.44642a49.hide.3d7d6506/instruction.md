# Bug Report

### Describe the bug

The "Max age (seconds)" field in the response template tag is showing up in situations where it shouldn't be visible. The visibility logic seems to be inverted or incorrectly configured - the field appears when it should be hidden and vice versa.

### Reproduction

When configuring a response template tag:

1. Set the trigger behavior to "always"
2. Select a field like "body" or "header"
3. Notice that the "Max age (seconds)" field is hidden even though it should be visible for cache expiration control

Alternatively:
1. Set the trigger behavior to "always" 
2. Select field as "raw" or "url"
3. The "Max age" field shows up even though these fields don't support age-based caching

### Expected behavior

The "Max age (seconds)" configuration should be visible when:
- Trigger behavior is set to "when-expired" (regardless of field type)
- Trigger behavior is set to "always" AND the field is NOT "raw" or "url"

The field should be hidden for simple fields like "raw" and "url" when using "always" trigger, since these don't use age-based caching.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
