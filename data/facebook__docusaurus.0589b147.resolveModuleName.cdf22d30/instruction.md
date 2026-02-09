# Bug Report

### Describe the bug

When trying to use a Docusaurus plugin/theme/preset with a shorthand name, I'm getting an error saying the module cannot be resolved, even though the package is properly installed in my `node_modules`.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    '@docusaurus/plugin-content-docs'
  ],
  themes: [
    '@docusaurus/theme-classic'
  ]
}
```

When I run the build, I get an error like:
```
Docusaurus was unable to resolve the "@docusaurus/plugin-content-docs" plugin. Make sure one of the following packages are installed:
- @docusaurus/plugin-content-docs
- plugin-content-docs
```

But the package IS installed and I can see it in my node_modules folder. If I check manually, `require.resolve('@docusaurus/plugin-content-docs')` works fine in Node.

### Expected behavior

Docusaurus should successfully resolve and load the plugin/theme when it's installed, not throw an error claiming it can't find it.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- Package manager: npm

This seems to have started happening recently. Previously the same config was working without issues.

---
Repository: /testbed
