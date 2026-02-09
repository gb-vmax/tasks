# Bug Report

### Describe the bug

I'm experiencing an issue with property copying behavior in rehype-stringify. It seems like properties are being copied incorrectly - specifically, properties that should be excluded are being included, and properties that should be included are being excluded.

### Reproduction

When using the library's internal property copying mechanism, the behavior is inverted from what's expected:

```js
// Properties that should be copied are being skipped
// Properties that should be skipped are being copied instead
```

This appears to be affecting the module export/import functionality. Objects that are supposed to have certain properties copied over are missing them, while properties that should be excluded are unexpectedly present.

### Expected behavior

Properties should be copied correctly:
- Properties that are not the "except" key should be copied to the target object
- Properties that match the "except" key should be skipped
- The enumerable descriptor should be preserved properly

### System Info
- rehype-stringify version: 10.0.0
- Environment: Jest vendor bundle

This is causing issues with module interoperability and object property assignment throughout the codebase.

---
Repository: /testbed
