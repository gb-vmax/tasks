# Bug Report

### Describe the bug

The redirect plugin is failing to properly check for existing files before creating redirects. It looks like the file existence check is not working as expected, which can lead to unexpected behavior when generating redirect files.

### Reproduction

```js
// Setup redirect configuration
const redirects = [
  {
    from: '/old-page',
    to: '/new-page',
  }
];

// When the plugin tries to write redirect files, the existence check
// doesn't properly await the file system operation
```

Steps to reproduce:
1. Configure redirects in your Docusaurus config
2. Run the build process
3. The plugin may not properly detect existing files before attempting to write redirects

### Expected behavior

The plugin should properly check if a file already exists at the redirect path before attempting to write to it. If a file exists, it should throw an error to prevent accidentally overwriting existing content.

### System Info
- Docusaurus plugin: docusaurus-plugin-client-redirects
- Node version: Latest

This seems to be related to async/await handling in the file existence check. The check might be executing synchronously when it should be waiting for the promise to resolve.

---
Repository: /testbed
