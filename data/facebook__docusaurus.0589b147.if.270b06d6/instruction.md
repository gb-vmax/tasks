# Bug Report

### Describe the bug

When using a function for `editUrl` in the docs plugin configuration, the edit URL is not being applied correctly. The edit button either doesn't appear or doesn't work as expected, even though a valid function is provided.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          editUrl: ({versionDocsDirPath, docPath}) => {
            return `https://github.com/myorg/myrepo/edit/main/${versionDocsDirPath}/${docPath}`;
          },
        },
      },
    ],
  ],
};
```

### Expected behavior

When `editUrl` is configured as a function, it should be used to generate edit URLs for documentation pages. The edit button should appear and link to the correct URL returned by the function.

### System Info

- Docusaurus version: 2.x
- Node version: 18.x

---
Repository: /testbed
