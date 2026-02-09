# Bug Report

### Describe the bug

I'm experiencing an issue with redirect file generation when `trailingSlash` is set to `false` and the redirect source path ends with `.html`. The plugin is creating redirect files in the wrong location, which causes file system conflicts.

### Reproduction

When configuring a redirect like this:

```js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          {
            from: '/old-page.html',
            to: '/new-page',
          },
        ],
      },
    ],
  ],
  trailingSlash: false,
};
```

The redirect file is being created at `/old-page.html/index.html` instead of `/old-page.html.html`.

### Expected behavior

When `trailingSlash` is `false` and the source path ends with `.html` (e.g., `/old-page.html`), the redirect file should be created at `/old-page.html.html` to avoid filesystem conflicts. On Unix systems, you can't have both a file and a folder with the same name like `old-page.html`.

The current behavior tries to create a folder named `old-page.html` and put an `index.html` inside it, which conflicts with the existing `old-page.html` file.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: Linux/macOS

---
Repository: /testbed
