# Bug Report

### Describe the bug

The extension redirects functionality is broken after a recent update. Paths that should generate redirects are no longer creating them, and the redirect system appears to be completely non-functional.

### Reproduction

When configuring the client redirects plugin with extension redirects:

```js
{
  fromExtensions: ['html', 'htm'],
}
```

Expected redirects are not being generated for paths like:
- `/docs/getting-started` should redirect to `/docs/getting-started.html`
- `/api/reference` should redirect to `/api/reference.html`

The redirects that should be created for adding file extensions to paths are not working at all.

### Expected behavior

The plugin should generate redirects from extension-less paths to paths with the specified extensions (e.g., `.html`, `.htm`). This was working correctly before but now no redirects are being created.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

---
Repository: /testbed
