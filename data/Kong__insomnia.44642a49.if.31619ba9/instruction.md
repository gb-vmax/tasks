# Bug Report

### Describe the bug

When working with gRPC service definitions, certain definitions are incorrectly being treated as service definitions when they should be filtered out. This causes issues when trying to introspect and work with proto files that contain both service definitions and message/enum types.

### Reproduction

```js
// Given a proto file with message and enum definitions
const definition = {
  // Either a message definition OR an enum definition
  // (not both at the same time)
}

// The definition is incorrectly identified as a service definition
// even when it's clearly a message or enum type
```

### Expected behavior

Message definitions and enum definitions should be properly excluded from being treated as service definitions. Currently, only definitions that are BOTH a message AND an enum simultaneously get filtered out, which is logically impossible and means valid message or enum definitions are passing through incorrectly.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
