# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar configuration in Docusaurus where nested sidebar items are being flattened incorrectly. When I define a sidebar with categories containing subcategories, all items end up at the same level instead of maintaining their hierarchical structure.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'intro',
        {
          type: 'category',
          label: 'Installation',
          items: ['install-npm', 'install-yarn']
        }
      ]
    }
  ]
}
```

With this configuration, the nested "Installation" category and its items appear at the same level as "intro" instead of being nested under "Getting Started".

### Expected behavior

The sidebar should maintain the proper nesting structure:
- Getting Started
  - intro
  - Installation
    - install-npm
    - install-yarn

Instead, it's rendering as:
- Getting Started
  - intro
  - install-npm
  - install-yarn

The nested category structure is being lost.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
