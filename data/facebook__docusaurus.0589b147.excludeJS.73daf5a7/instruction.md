# Bug Report

### Describe the bug

After a recent update, JavaScript files in the Docusaurus client directory are no longer being transpiled correctly. This causes build failures when using modern JavaScript syntax in nested directories.

### Reproduction

1. Create a custom component in a nested client directory structure
2. Use ES6+ syntax in the component
3. Build the project

Example directory structure:
```
website/
  node_modules/
    @docusaurus/
      theme-classic/
        lib/
          client/
            theme/
              MyComponent.jsx
```

The transpilation seems to fail for files that contain the client directory path anywhere in their full path, not just at the beginning. This affects Docusaurus packages installed in node_modules.

### Expected behavior

All JavaScript files in Docusaurus client directories should be transpiled regardless of where they appear in the path hierarchy. Previously, files were correctly transpiled when the path started with the client directory.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- Build tool: Webpack

---
Repository: /testbed
