# Bug Report

### Describe the bug

I'm encountering an issue with the `resolve` function in the plugin context where the `skipSelf` parameter behavior seems to be inverted. When I explicitly set `skipSelf: true`, the plugin still resolves itself, and when I set `skipSelf: false`, it skips itself.

### Reproduction

```js
// In a custom plugin
{
  name: 'my-plugin',
  resolveId(source, importer) {
    // Try to resolve with skipSelf explicitly set to true
    const result = this.resolve(source, importer, { skipSelf: true });
    // Expected: should skip this plugin
    // Actual: this plugin is still called
  }
}
```

The behavior is backwards from what the parameter name suggests. When `skipSelf` is `true`, I expect the current plugin to be skipped during resolution, but it's not being skipped.

### Expected behavior

- `skipSelf: true` should skip the current plugin during resolution
- `skipSelf: false` should allow the current plugin to be called during resolution
- The default behavior (when `skipSelf` is not specified) should skip the current plugin

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
