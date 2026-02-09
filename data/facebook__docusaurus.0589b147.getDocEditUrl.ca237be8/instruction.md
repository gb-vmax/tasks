# Bug Report

### Describe the bug

The edit URL functionality is broken when using a function for the `editUrl` option in the docs plugin configuration. Instead of calling the function when `editUrl` is a function, it seems to be doing the opposite - trying to call it when it's NOT a function, which causes errors.

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

When building or serving the site with this configuration, the edit URLs are not generated correctly. The function is never called, and you get unexpected behavior.

### Expected behavior

When `editUrl` is configured as a function, it should be invoked with the appropriate parameters (version, docPath, permalink, etc.) to generate the edit URL for each doc. The function approach should work as documented for customizing edit URLs based on the document metadata.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like a regression as the function-based `editUrl` was working in previous versions. The logic for checking the type of `editUrl` appears to be inverted.

---
Repository: /testbed
