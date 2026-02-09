# Bug Report

### Describe the bug

When creating a new documentation version with an empty or whitespace-only name, the validation is not working as expected. The system should reject version names that contain only whitespace characters, but it's currently accepting them instead.

### Reproduction

```js
// This should throw an error but doesn't
validateVersionName('   ')

// This should also throw an error
validateVersionName('\t\n')
```

When trying to create a version with a name that's just spaces or whitespace, the validation passes when it should fail. This can lead to issues with the file system and version management.

### Expected behavior

Version names containing only whitespace characters should be rejected with an error message like:
```
Invalid version name "   ": version name must contain at least one non-whitespace character.
```

### Additional context

This seems to affect the docs plugin version validation. I noticed this when accidentally trying to create a version with just spaces in the name, and it was accepted without any error.

---
Repository: /testbed
