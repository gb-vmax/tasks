# Bug Report

### Describe the bug

The redirect page template is not rendering correctly - it seems like the template data is not being passed properly to the compiled template function. When creating redirect pages, the generated HTML is missing important metadata and configuration options.

### Reproduction

When using the client redirects plugin to create a redirect from one page to another:

```js
// In docusaurus.config.js
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
]
```

The generated redirect page only contains the `toUrl` property but is missing other critical template variables like `searchAnchorForwarding` and other configuration data that should be available in the template.

### Expected behavior

The redirect page template should receive all the necessary data including:
- `toUrl` - the destination URL
- `searchAnchorForwarding` - whether to forward search params and anchors
- Any other template configuration options

All of these should be accessible within the template for proper redirect page generation.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

---
Repository: /testbed
