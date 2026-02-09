# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar categories in the docs plugin. When using the shorthand object notation for defining sidebar categories, the items within each category are not being rendered correctly. Instead of showing the actual content items, the category label itself appears to be used as the items value.

### Reproduction

```js
// sidebars.js
module.exports = {
  mySidebar: {
    'Getting Started': ['intro', 'installation'],
    'Advanced': ['config', 'deployment']
  }
}
```

When I use this shorthand format, the sidebar doesn't display the docs properly. The category shows up but the nested items don't appear as expected.

### Expected behavior

The sidebar should expand to show the items array under each category. For example, the 'Getting Started' category should contain links to 'intro' and 'installation' docs.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
