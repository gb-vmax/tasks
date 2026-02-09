# Bug Report

### Describe the bug

I'm experiencing an issue with plugin version detection in Docusaurus. When a plugin is located outside the site directory (e.g., in a parent directory or a completely different path), the build process seems to hang or fail to properly detect the plugin's metadata.

### Reproduction

1. Create a Docusaurus site in `/home/user/my-site`
2. Create a custom plugin in a parent directory like `/home/user/my-plugin`
3. Reference the plugin using a relative path in `docusaurus.config.js`:

```js
module.exports = {
  plugins: [
    '../my-plugin'
  ]
}
```

4. Try to build or start the development server

The process appears to get stuck or takes an unusually long time when trying to resolve the plugin's package information.

### Expected behavior

The plugin should be properly detected and classified as either a local plugin or package plugin based on its location and package.json file, regardless of whether it's inside or outside the site directory.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: Linux/macOS

This seems to happen specifically when the plugin path traverses outside the site directory. Plugins within the site directory work fine.

---
Repository: /testbed
