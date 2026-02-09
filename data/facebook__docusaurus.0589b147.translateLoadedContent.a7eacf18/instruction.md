# Bug Report

### Describe the bug

After a recent update, the documentation plugin is not loading versions correctly. The sidebar shows an empty or malformed version list, and navigation between different doc versions is broken.

### Reproduction

When building a docs site with multiple versions:

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          versions: {
            current: {
              label: '2.0.0',
            },
            '1.0.0': {
              label: '1.0.0',
            },
          },
        },
      },
    ],
  ],
};
```

The version dropdown doesn't render properly and trying to navigate between versions results in errors or unexpected behavior.

### Expected behavior

The version selector should display all available versions and allow switching between them. The `loadedVersions` data structure should contain an array of version objects that can be properly iterated over.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
