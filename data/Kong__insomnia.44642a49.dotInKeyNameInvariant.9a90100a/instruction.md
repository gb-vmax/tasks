# Bug Report

### Describe the bug

When importing data with keys that contain dots (e.g., `"some.key"`), the validation is not working as expected. The current implementation seems to only reject keys that are exactly a single dot `"."` instead of checking if a dot appears anywhere within the key name.

### Reproduction

```js
const testData = {
  "user.name": "John",
  "config.setting": "value"
};

// This should throw an error but doesn't
dotInKeyNameInvariant(testData);
```

### Expected behavior

The validator should throw an error for any key that contains a dot character anywhere in the key name (like `"user.name"` or `"config.setting"`), not just keys that are exactly equal to `"."`.

The error message suggests this is the intended behavior: `"Detected invalid key "${key}", which contains '.'"` - note it says "contains" not "is".

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
