# Bug Report

### Describe the bug

When creating redirects for paths ending with `.html`, the plugin is generating incorrect redirect file paths. Instead of creating a redirect file at the expected location (e.g., `/xyz.html.html` for a source path `/xyz.html`), it's now writing to `/xyz.html`, which causes the redirect file to overwrite the original file.

### Reproduction

```js
// Configuration with trailingSlash: false
{
  redirects: [
    {
      from: '/old-page.html',
      to: '/new-page'
    }
  ]
}
```

When the plugin processes this redirect:
1. The source path is `/old-page.html`
2. The redirect file is created at `/old-page.html` instead of `/old-page.html.html`
3. This overwrites any existing file at that location

### Expected behavior

For paths ending with `.html` when `trailingSlash` is `false`, the redirect file should be created at a path like `/xyz.html.html` to avoid conflicts with existing files. This was the previous behavior that prevented file/folder naming conflicts on Unix filesystems.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken after a recent change to the redirect file path logic. The old behavior correctly handled the edge case where a file and folder can't share the same name on Unix systems.

---
Repository: /testbed
