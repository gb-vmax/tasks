# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when accessing the deprecated `name` property on emitted assets in the bundle. The application crashes with a "Maximum call stack size exceeded" error.

### Reproduction

```js
// In generateBundle hook
generateBundle(options, bundle) {
  for (const fileName in bundle) {
    const asset = bundle[fileName];
    // Accessing the deprecated name property causes stack overflow
    console.log(asset.name);
  }
}
```

When trying to access `asset.name`, the getter appears to call itself recursively instead of returning the actual name value, leading to a stack overflow.

### Expected behavior

The deprecated `name` property should return the asset's name value (with a deprecation warning) rather than causing infinite recursion. It should work the same way as before, just with the deprecation notice.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
