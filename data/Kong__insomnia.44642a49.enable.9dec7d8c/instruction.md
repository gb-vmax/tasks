# Bug Report

### Describe the bug

After a recent update, the curl mock implementation seems to have changed how features are stored. I'm experiencing issues where feature flags that were previously working are now causing problems in my application.

### Reproduction

```js
const curl = new Curl();
curl.enable('SOME_FEATURE');

// Previously this would work, but now it fails
if (curl._features['SOME_FEATURE']) {
  // This condition behaves unexpectedly
}
```

When checking if a feature is enabled, the code expects a boolean value but now receives an object instead. This breaks any code that was relying on the feature flag being a simple truthy value.

### Expected behavior

When enabling a feature with `curl.enable()`, the feature should be stored as a boolean `true` value, not as an object. Code checking `if (curl._features[featureName])` should continue to work as before.

### System Info
- Package: @getinsomnia/node-libcurl (mock)
- Insomnia version: latest

---
Repository: /testbed
