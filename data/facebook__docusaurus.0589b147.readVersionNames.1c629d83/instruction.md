# Bug Report

### Describe the bug

When `disableVersioning` is set to `true` in the docs plugin options, the current version is still being added to the versions array. This seems to ignore the `disableVersioning` configuration and includes the current version anyway.

### Reproduction

```js
// docusaurus.config.js
{
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          disableVersioning: true,
          includeCurrentVersion: true,
        },
      },
    ],
  ],
}
```

With this configuration, I would expect versioning to be completely disabled, but the current version still gets included in the versions list.

### Expected behavior

When `disableVersioning: true` is set, no versions should be included regardless of other settings like `includeCurrentVersion`. The plugin should respect the `disableVersioning` flag and return an empty versions array.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
