# Bug Report

### Describe the bug

I'm encountering an issue with sidebar validation in Docusaurus. It appears that sidebar validation is now happening before the sidebars are fully processed, which causes problems when the sidebar structure contains references or dependencies that need to be resolved first.

### Reproduction

Create a sidebar configuration with category metadata:

```js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Guides',
      items: [
        'intro',
        'getting-started'
      ]
    }
  ]
};
```

When the sidebar processor runs, validation occurs on the unprocessed sidebar structure instead of the final processed structure. This means any transformations or resolutions that happen during processing aren't taken into account during validation.

### Expected behavior

Validation should occur after sidebars have been fully processed and all references/metadata have been resolved. This ensures that the validation checks are run against the final sidebar structure that will actually be used.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
