# Bug Report

### Describe the bug

I'm encountering an issue with version name validation in the docs plugin. It seems like the validation logic is inverted - versions with only whitespace are being accepted when they should be rejected, and valid versions are being rejected.

### Reproduction

```js
// This should fail but doesn't
validateVersionName('   ')  // Only whitespace - should throw error but passes

// This should pass but doesn't  
validateVersionName('1.0.0')  // Valid version name - should pass but throws error
```

### Expected behavior

- Version names containing only whitespace characters should be rejected with an error
- Valid version names with actual content should be accepted
- The validation should properly check that version names contain at least one non-whitespace character

### Additional context

This appears to affect the version naming validation when creating new doc versions. The current behavior makes it possible to create versions with blank names, which causes issues downstream.

---
Repository: /testbed
