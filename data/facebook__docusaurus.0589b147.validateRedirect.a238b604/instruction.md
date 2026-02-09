# Bug Report

### Describe the bug

The redirect validation in `docusaurus-plugin-client-redirects` is throwing errors for valid redirect configurations. When I configure redirects correctly, the plugin crashes with a validation error instead of accepting them.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          {
            from: '/old-page',
            to: '/new-page',
          },
        ],
      },
    ],
  ],
};
```

When running the build, it throws:
```
Error: {"from":"/old-page","to":"/new-page"} => Validation error: ...
```

### Expected behavior

Valid redirects should be accepted without throwing validation errors. The plugin should only throw errors when there are actual validation issues with the redirect configuration.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The redirects worked fine before but now every valid redirect configuration is being rejected.

---
Repository: /testbed
