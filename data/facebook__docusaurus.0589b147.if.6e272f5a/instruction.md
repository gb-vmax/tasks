# Bug Report

### Describe the bug

When using the docs plugin with `editUrl` configured, the edit URL functionality is not working as expected. The edit URL is not being generated correctly when `editUrl` is provided as a string value.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          editUrl: 'https://github.com/myorg/myrepo/edit/main/',
        },
      },
    ],
  ],
};
```

After configuring the `editUrl` option with a string value, the edit links on documentation pages are not being rendered. The expected behavior is that each doc page should have an "Edit this page" link pointing to the GitHub repository.

### Expected behavior

When `editUrl` is provided as a string, the plugin should generate proper edit URLs for each documentation page by combining the base `editUrl` with the relative path to the document.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
