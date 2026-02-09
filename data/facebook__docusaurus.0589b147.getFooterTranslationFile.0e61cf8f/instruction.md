# Bug Report

### Describe the bug

When using multi-column footer links in Docusaurus theme classic, the translation keys are being generated incorrectly. The system is trying to access `link.title` instead of `link.label` when filtering and creating translation keys, which causes footer link labels to not be properly extracted for translation.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  themeConfig: {
    footer: {
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: '/docs/intro',
            },
            {
              label: 'Tutorial',
              to: '/docs/tutorial',
            },
          ],
        },
      ],
    },
  },
};
```

With this configuration, the footer link labels are not being processed correctly for translation. The translation file generation seems to be looking for a `title` property on the link items instead of the `label` property.

### Expected behavior

Footer link items should be filtered by their `label` property and translation keys should be generated using `link.label`, not `link.title`. The translation keys should be created correctly for all footer links that have labels defined.

### System Info
- Docusaurus version: latest
- Theme: @docusaurus/theme-classic

---
Repository: /testbed
