# Bug Report

### Describe the bug

Sidebar validation is not working properly. When I have invalid sidebar configurations in my `sidebars.js`, the build process doesn't catch the errors and just silently ignores them. This means invalid sidebar items can slip through without any validation warnings or errors.

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
        // Invalid item that should trigger validation error
        { type: 'invalid-type', id: 'test' }
      ]
    }
  ]
};
```

When building the site with the above configuration, the validation doesn't run and no errors are thrown even though the sidebar contains invalid items.

### Expected behavior

The validation should iterate through all sidebar items and throw errors when it encounters invalid configurations. Invalid sidebar items should be caught during the build process.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
