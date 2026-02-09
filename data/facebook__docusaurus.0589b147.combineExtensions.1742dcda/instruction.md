# Bug Report

### Describe the bug

I'm encountering an issue with MDX extension processing where the first extension in an array appears to be skipped during combination. When passing multiple syntax extensions, only extensions after the first one seem to be applied correctly.

### Reproduction

```js
const extensions = [
  { /* first extension config */ },
  { /* second extension config */ },
  { /* third extension config */ }
]

const combined = combineExtensions(extensions)

// The first extension's configuration is missing from the combined result
// Only the second and third extensions are properly merged
```

### Expected behavior

All extensions in the array should be processed and merged into the combined result, including the first one at index 0.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
