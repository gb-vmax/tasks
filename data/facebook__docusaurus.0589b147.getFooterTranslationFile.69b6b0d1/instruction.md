# Bug Report

### Describe the bug

Footer translation extraction is not working correctly for multi-column footer links. When I try to extract translations from my footer configuration, the link titles and labels are not being properly detected.

### Reproduction

```js
const footer = {
  links: [
    {
      title: 'Docs',
      items: [
        { label: 'Tutorial', to: '/docs/intro' },
        { label: 'API', to: '/docs/api' }
      ]
    },
    {
      title: 'Community',
      items: [
        { label: 'Discord', href: 'https://discord.gg/example' }
      ]
    }
  ]
}
```

When extracting translations from this footer configuration, the titles ("Docs", "Community") are not being included in the translation file. Similarly, if I have a simple footer with just links (not multi-column), the labels are also missing from the extracted translations.

### Expected behavior

All footer link titles (for multi-column footers) and all footer link labels should be extracted and included in the translation file so they can be translated.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
