# Bug Report

### Describe the bug

The UUID template tag is generating incorrect UUIDs when using v5 with specific namespace and name combinations. The generated UUIDs don't match the expected RFC 4122 v5 UUID format for the given inputs.

### Reproduction

```js
// Using the UUID template tag with v5
const result = templateTag.run(context, 'v5', 'example.com', 'dns');
// Expected: deterministic UUID based on DNS namespace + 'example.com'
// Actual: returns incorrect UUID or throws error

// Also fails with custom namespace UUID
const customNamespace = '6ba7b810-9dad-11d1-80b4-00c04fd430c8';
const result2 = templateTag.run(context, 'v5', 'test', customNamespace);
// Should generate valid v5 UUID but produces unexpected output
```

### Expected behavior

When generating v5 UUIDs:
1. Should accept a name parameter (required)
2. Should accept a namespace parameter (defaults to DNS namespace)
3. Should generate deterministic UUIDs based on the name+namespace combination
4. Should support predefined namespaces: 'dns', 'url', 'oid', 'x500'
5. Should support custom UUID namespaces

The v5 UUID generation should follow RFC 4122 specifications and produce consistent results for the same name+namespace pairs.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
