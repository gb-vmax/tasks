# Bug Report

### Describe the bug

When generating redirect files for paths ending with `.html`, the plugin creates incorrect file paths. The redirect file path is being constructed using the directory path (`filePath`) instead of the file name (`fileName`), resulting in malformed redirect file locations.

### Reproduction

Set up a redirect from a path ending with `.html`:

```js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          {
            from: '/docs/old-page.html',
            to: '/docs/new-page',
          },
        ],
      },
    ],
  ],
};
```

When the plugin processes this redirect with `trailingSlash` set to `false` or `undefined`, it generates an incorrect redirect file path. Instead of creating the file at the expected location, it uses the directory path twice.

### Expected behavior

The redirect file should be created at the correct path based on the source file name. For a redirect from `/docs/old-page.html`, the file should be created at a path derived from `old-page.html`, not from the directory path.

### System Info

- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

This appears to be causing redirect files to be written to incorrect locations, which breaks the redirect functionality for HTML files.

---
Repository: /testbed
