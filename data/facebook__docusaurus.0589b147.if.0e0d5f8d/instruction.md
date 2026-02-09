# Bug Report

### Describe the bug

When `editUrl` is not provided in the docs plugin options (i.e., it's `undefined` or `null`), the edit URL is not being generated even when it should be. The edit functionality appears to be completely disabled when `editUrl` is falsy, but it should still work with default behavior in certain cases.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        // editUrl is not specified (undefined)
        path: 'docs',
        editCurrentVersion: false,
      },
    ],
  ],
};
```

With this configuration, the edit URLs are not being generated for versioned docs even though the content path is available and should be used to construct the edit URL.

### Expected behavior

When `editUrl` is not a function, the plugin should still attempt to generate edit URLs using the content path, unless `editUrl` is explicitly set to `false` or a function is provided. Only when `editUrl` is a function should it return undefined edit URLs (since the function has full control).

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
