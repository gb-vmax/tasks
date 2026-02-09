# Bug Report

### Describe the bug

When using plugins or themes with invalid configuration, the error messages display incorrect paths. The path shown in the error message doesn't properly handle array indices and shows them as string concatenations instead of array notation.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        someInvalidConfig: 'value'
      }
    ]
  ]
}
```

When running Docusaurus with an invalid plugin configuration that contains nested properties or array indices, the error path is formatted incorrectly. For example, if there's an error in a plugin at index 0, the path might show something like `.0` instead of `[0]`.

### Expected behavior

Error messages should display proper paths with correct array notation (e.g., `plugins[0].someProperty`) instead of treating array indices as string properties (e.g., `plugins.0.someProperty`).

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
