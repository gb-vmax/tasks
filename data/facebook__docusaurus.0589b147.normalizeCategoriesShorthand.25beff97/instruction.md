# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar category shorthand notation where the label and items appear to be swapped. When defining a sidebar using the object shorthand syntax, the category labels are showing the item values instead of the keys, and vice versa.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: {
    'Getting Started': ['intro', 'installation'],
    'Advanced': ['configuration', 'deployment']
  }
}
```

With this configuration, the sidebar is rendering incorrectly:
- The category label shows `['intro', 'installation']` instead of "Getting Started"
- The items are being set to "Getting Started" instead of the actual doc IDs

### Expected behavior

The sidebar should render with:
- Category label: "Getting Started"
- Items: `['intro', 'installation']`

But instead it's rendering with the label and items swapped.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
