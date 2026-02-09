# Bug Report

### Describe the bug

When using nested sidebar categories in Docusaurus docs, the validation doesn't seem to be working properly for items inside categories. I have a sidebar configuration with nested categories and items, but I'm not getting any validation errors even when I have invalid items nested inside.

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
          label: 'Advanced',
          items: [
            'invalid-item-that-should-fail-validation'
          ]
        }
      ]
    }
  ]
};
```

### Expected behavior

The sidebar validation should recursively check all nested items within categories and throw validation errors for invalid configurations. Currently it seems like items nested inside categories are not being validated at all.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
