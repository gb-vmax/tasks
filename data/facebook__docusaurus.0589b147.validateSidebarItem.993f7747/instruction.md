# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar validation where nested category items are not being validated properly. When I have a sidebar with categories containing multiple items, only the first item in each category gets validated and the rest are silently skipped.

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
        'installation',
        'configuration'
      ]
    }
  ]
}
```

With this configuration, if there's an invalid item after the first one (like 'installation' or 'configuration'), the validation doesn't catch it and the build continues without errors.

### Expected behavior

All items within a category should be validated, not just the first one. If any item in the category is invalid, validation should fail with an appropriate error message.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
