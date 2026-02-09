# Bug Report

### Describe the bug

I'm experiencing an issue with the automock functionality where it's incorrectly identifying proto types. The type checking logic seems to be broken and is returning `true` for cases where it should return `false`.

### Reproduction

When trying to use automock with gRPC definitions, the type resolution fails because the `isProtoType` function is not properly validating whether a resolved type is actually a valid proto Type object.

Steps to reproduce:
1. Set up a gRPC request with a message that has nested types
2. Try to generate mock data using the automock feature
3. The function incorrectly identifies null or undefined values as valid proto types

This causes the automock to fail when it tries to access properties on null/undefined objects that it thinks are valid Type instances.

### Expected behavior

The `isProtoType` function should return `false` when the `resolvedType` is `null` or `undefined`, and only return `true` when it's actually a valid Type object with the appropriate properties like `fieldsArray`.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
