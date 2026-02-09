# Bug Report

### Describe the bug

I'm experiencing an issue where sidebar validation is not catching errors in my sidebar configuration. It seems like invalid sidebar structures are being processed without throwing validation errors, which causes problems later in the build process.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        // Invalid item structure that should be caught
        {
          type: 'invalid-type',
          id: 'some-doc'
        }
      ]
    }
  ]
};
```

When I build my Docusaurus site with this configuration, the validation doesn't catch the invalid sidebar item type early on. Instead, errors occur much later during the build process, making it harder to debug what went wrong.

### Expected behavior

The sidebar validation should catch structural errors in the sidebar configuration before processing begins, providing clear error messages about what's wrong with the configuration.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
