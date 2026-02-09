# Bug Report

### Describe the bug

I'm experiencing an issue with footer link translation extraction in the classic theme. When using multi-column footer links, the translation system seems to be checking for the wrong property when filtering links.

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
              label: 'API Reference',
              to: '/docs/api',
            },
          ],
        },
      ],
    },
  },
};
```

With this configuration, the footer links with `label` properties are not being properly extracted for translation. It appears the code is looking for a `title` property on individual link items instead of `label`, which causes links to be filtered out incorrectly.

### Expected behavior

Footer links with `label` properties should be included in the translation file generation, regardless of whether they're in a multi-column or single-column footer layout.

### System Info

- Docusaurus version: latest
- Theme: @docusaurus/theme-classic

---
Repository: /testbed
