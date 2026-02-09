# Bug Report

### Describe the bug

I'm experiencing an issue with plugin caching where plugins with duplicate names are being cached when they shouldn't be. This is causing unexpected behavior in my build process where plugins that should be treated as separate instances are being incorrectly reused.

### Reproduction

```js
const rollup = require('rollup');

// Create two plugins with the same name
const plugin1 = {
  name: 'my-plugin',
  transform(code) {
    return code + '// plugin1';
  }
};

const plugin2 = {
  name: 'my-plugin',
  transform(code) {
    return code + '// plugin2';
  }
};

// Use both plugins in the build
rollup.rollup({
  input: 'src/index.js',
  plugins: [plugin1, plugin2]
});
```

### Expected behavior

When multiple plugins share the same name (and don't have a `cacheKey` defined), they should not be cached. Each plugin instance should be treated independently, and `cacheable` should be set to `false` for plugins with duplicate names.

### Actual behavior

Plugins with duplicate names are being cached incorrectly, leading to one plugin being used in place of another.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
