# Bug Report

### Describe the bug

I'm experiencing an issue with navbar item translations in the classic theme. It seems like navbar items with labels are not being included in the translation file, which means they can't be translated properly.

### Reproduction

```js
// In docusaurus.config.js
navbar: {
  items: [
    {
      type: 'doc',
      docId: 'intro',
      label: 'Documentation',
    },
    {
      type: 'dropdown',
      label: 'Community',
      items: [
        {
          label: 'Discord',
          href: 'https://discord.gg/example',
        },
      ],
    },
  ],
}
```

After running the site, the translation files don't include entries for "Documentation" or "Community" labels, making it impossible to translate these navbar items.

### Expected behavior

All navbar items with labels should be included in the translation file so they can be properly localized. The generated translation file should contain entries like:
```
item.label.Documentation
item.label.Community
item.label.Discord
```

### System Info
- Docusaurus version: latest
- Theme: @docusaurus/theme-classic

---
Repository: /testbed
