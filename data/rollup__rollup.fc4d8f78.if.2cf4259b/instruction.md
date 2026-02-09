# Bug Report

### Describe the bug

I'm encountering an issue with dynamic imports when using the CommonJS output format. It appears that dynamic imports with external module resolutions are being incorrectly handled - they're returning `{ helper: null, mechanism: null }` even when they shouldn't.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    format: 'cjs',
    file: 'dist/bundle.js'
  },
  external: ['some-external-module']
}

// src/index.js
async function loadModule() {
  const module = await import('some-external-module');
  return module;
}
```

When bundling with the above configuration, the dynamic import doesn't get the proper interop helpers applied even though the resolution is an ExternalModule instance.

### Expected behavior

Dynamic imports of external modules in CJS format should receive the appropriate helper and mechanism based on the interop settings, not just return null values. The interop helper should be determined by calling `getInteropHelper(resolution, exportMode, interop)` for external module resolutions.

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
