# Bug Report

### Describe the bug

When using a functional `editUrl` in the docs plugin configuration, the edit URLs are not being generated correctly. The plugin seems to be treating functional edit URLs differently than expected, and the localized edit URL is missing from the version metadata.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          editUrl: ({docPath}) => {
            return `https://github.com/myorg/myrepo/edit/main/docs/${docPath}`;
          },
        },
      },
    ],
  ],
};
```

With this configuration, the edit button functionality is broken. The version metadata doesn't include the `editUrlLocalized` property that should be present.

### Expected behavior

When providing a functional `editUrl`, the plugin should still properly set up the version metadata including both `editUrl` and `editUrlLocalized` properties. The functional form should be respected and passed through correctly.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
