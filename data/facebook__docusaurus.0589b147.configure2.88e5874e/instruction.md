# Bug Report

### Describe the bug

I'm experiencing an issue with nested extensions not being applied correctly when using the markdown processor. It seems like extension configurations are not being merged properly into the base configuration, and instead extensions are being applied to themselves recursively.

### Reproduction

```js
const processor = remark()
  .use(plugin1)
  .use(plugin2, {
    extensions: [
      { someOption: 'value1' },
      { anotherOption: 'value2' }
    ]
  });

// The base configuration doesn't receive the nested extension options
// Instead, the extensions seem to be configured incorrectly
```

When I have a plugin with nested extensions, the configuration doesn't propagate as expected. The first extension in the array is skipped entirely, and subsequent extensions don't get merged into the base configuration.

### Expected behavior

All nested extensions should be properly merged into the base configuration object. Each extension in the `extensions` array should be processed and its properties should be added to the base.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
