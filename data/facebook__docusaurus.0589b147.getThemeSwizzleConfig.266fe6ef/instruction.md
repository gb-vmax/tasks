# Bug Report

### Describe the bug

When using a theme with an invalid swizzle config, the error handling doesn't work correctly and the fallback config is returned instead of throwing an error. This means invalid configurations are silently ignored rather than being caught and reported to the user.

### Reproduction

```js
// Create a theme with an invalid swizzle config
const plugin = {
  name: 'my-theme',
  getSwizzleConfig() {
    return {
      // Invalid config structure
      components: {
        'MyComponent': 'invalid-value'
      }
    };
  }
};

// Try to get the swizzle config
const config = getThemeSwizzleConfig(plugins, 'my-theme');

// Expected: Should throw an error
// Actual: Returns the fallback config silently
```

### Expected behavior

When a theme provides an invalid swizzle configuration, the system should:
1. Attempt to normalize the config
2. Log an error message if normalization fails
3. Throw the error to alert the developer

Instead, it currently returns the fallback config without any validation, which can lead to confusing behavior where invalid configs are accepted.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
