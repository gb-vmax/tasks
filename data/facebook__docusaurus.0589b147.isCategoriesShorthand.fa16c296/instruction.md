# Bug Report

### Describe the bug

I'm experiencing an issue with the sidebar configuration where categories shorthand syntax is not being recognized correctly. When I define sidebars using the object shorthand notation (without explicit `type` field), the items are not being processed as category shortcuts.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      'Getting Started': ['intro', 'installation'],
      'Advanced': ['api', 'configuration']
    }
  ]
}
```

When using this shorthand syntax for categories (object without `type` property), the sidebar doesn't render properly. It seems like the shorthand detection logic is inverted - it's treating objects WITH a type as shorthand and rejecting objects WITHOUT a type.

### Expected behavior

The sidebar should recognize objects without a `type` field as categories shorthand and process them accordingly. This is the documented way to define category shortcuts in the Docusaurus sidebar configuration.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
