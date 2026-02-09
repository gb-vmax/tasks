# Bug Report

### Describe the bug

I'm experiencing an issue with MDX extension handling where multiple extensions don't seem to be combining properly. When I register multiple syntax extensions, only the last one appears to be active, and earlier extensions are being ignored or overwritten.

### Reproduction

```js
const extension1 = {
  flow: { /* custom flow syntax */ }
}

const extension2 = {
  text: { /* custom text syntax */ }
}

const combined = combineExtensions([extension1, extension2])

// Expected: combined should have both 'flow' and 'text' properties
// Actual: only properties from extension2 are present
```

### Expected behavior

When combining multiple MDX extensions, all extensions should be merged together so that each extension's syntax rules are preserved. Currently it seems like extensions are overwriting each other instead of being properly combined.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
