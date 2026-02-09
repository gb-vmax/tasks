# Bug Report

### Describe the bug

I'm experiencing an issue with the navbar translation extraction where nested navbar items are being duplicated or not properly flattened. When I have a navbar with dropdown items, the translation file seems to include items multiple times or in an unexpected structure.

### Reproduction

```js
const navbar = {
  items: [
    {
      label: 'Docs',
      to: '/docs',
    },
    {
      label: 'Community',
      items: [
        {
          label: 'Discord',
          to: '/discord',
        },
        {
          label: 'Twitter',
          to: '/twitter',
        }
      ]
    }
  ]
}
```

When processing this navbar structure for translations, the flattening logic appears to create duplicates or miss certain items entirely. The parent items and their nested children aren't being handled correctly.

### Expected behavior

The navbar flattening should correctly extract all navbar items (both parent and nested items) exactly once without duplication, so that translation keys are generated properly for all menu items.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
