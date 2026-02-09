# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar categories when using the shorthand notation. The labels and items appear to be swapped - the category label shows the items array and the items show what should be the label.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: {
    'Getting Started': ['intro', 'installation'],
    'Advanced': ['api', 'configuration']
  }
}
```

When I use this shorthand format, the sidebar renders incorrectly:
- The category label displays the array items (e.g., shows `['intro', 'installation']` as the label)
- The items section shows the label string (e.g., 'Getting Started' appears where the doc items should be)

### Expected behavior

The sidebar should display:
- Category label: "Getting Started"
- Items: intro, installation
- Category label: "Advanced"  
- Items: api, configuration

Instead it's showing the values in reverse - labels where items should be and items where labels should be.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
