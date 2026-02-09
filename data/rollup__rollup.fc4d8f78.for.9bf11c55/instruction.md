# Bug Report

### Describe the bug

I'm experiencing an issue where the cache option is being incorrectly handled in the CLI. When I explicitly set `cache: false` in my rollup config, it gets changed to `undefined` instead of being preserved as `false`. This causes unexpected behavior as `undefined` and `false` have different semantics in Rollup's caching logic.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  },
  cache: false  // Explicitly disable cache
}
```

Run the build via CLI:
```bash
rollup -c
```

The config option `cache: false` is being transformed to `cache: undefined` internally, which doesn't respect the explicit `false` value I've set.

### Expected behavior

When I explicitly set `cache: false` in my configuration, it should remain as `false` and not be changed to `undefined`. The CLI should only modify the cache option when it's not explicitly set by the user.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

This seems to have changed in a recent update. Previously, explicitly setting `cache: false` worked as expected.

---
Repository: /testbed
