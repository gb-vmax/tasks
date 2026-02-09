# Bug Report

### Describe the bug

I'm experiencing an issue with version translations where the translation files are not being generated correctly. It seems like the structure of the returned translation files is wrong - instead of getting a flat array of translation files, I'm getting nested arrays.

### Reproduction

When using multiple versions in the docs plugin configuration:

```js
{
  versions: [
    { name: 'v1', ... },
    { name: 'v2', ... },
    { name: 'v3', ... }
  ]
}
```

The translation files returned have an unexpected nested structure. Each version's translation files should be merged into a single flat array, but instead they appear to be wrapped in additional array layers.

### Expected behavior

The function should return a flat array of all translation files from all versions combined, not a nested array structure. Each version's translation files should be properly flattened and mapped.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
