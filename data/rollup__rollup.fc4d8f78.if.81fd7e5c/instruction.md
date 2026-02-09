# Bug Report

### Describe the bug

I'm experiencing an issue with plugin caching behavior. It seems like plugins that should not be cacheable are being cached, and vice versa. Specifically, anonymous plugins are now being treated as cacheable when they shouldn't be.

### Reproduction

```js
// Create a plugin without a cacheKey
const myPlugin = {
  name: 'rollup-plugin-test',
  transform(code) {
    // plugin logic
  }
}

// Use the same plugin name multiple times
const config = {
  plugins: [
    myPlugin,
    myPlugin  // This should not be cached but appears to be
  ]
}
```

When using plugins with duplicate names or anonymous plugins, the caching logic doesn't work as expected. Plugins that should be marked as non-cacheable are being cached, leading to unexpected behavior during the build process.

### Expected behavior

- Anonymous plugins (those starting with the anonymous prefix) should not be cacheable
- Plugins with duplicate names should not be cacheable
- Only plugins with unique names and explicit cacheKey should be cacheable

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
