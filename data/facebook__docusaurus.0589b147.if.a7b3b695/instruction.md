# Bug Report

### Describe the bug

The redirect plugin is overwriting existing files when it shouldn't. I have a custom HTML file at a specific path, and after building my site, the redirect plugin completely replaces it with a redirect file. This causes my custom content to be lost.

### Reproduction

1. Create a static HTML file in your build output directory (e.g., `build/custom-page/index.html`)
2. Configure a redirect that points to the same path
3. Run the build process
4. The original `index.html` file gets overwritten by the redirect HTML

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          {
            to: '/docs/introduction',
            from: '/custom-page',
          },
        ],
      },
    ],
  ],
};
```

### Expected behavior

The plugin should detect that a file already exists at the target path and either skip creating the redirect or throw an error to prevent overwriting existing content. My custom HTML files should not be replaced.

### System Info

- Docusaurus version: Latest
- Node version: 18.x

This is causing data loss in production builds. Any help would be appreciated!

---
Repository: /testbed
