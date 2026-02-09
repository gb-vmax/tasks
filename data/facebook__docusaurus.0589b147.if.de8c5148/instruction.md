# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar rendering where nested category items are not displaying correctly. The sidebar structure appears to be broken - instead of showing the nested items properly, they seem to be wrapped in an extra array level.

### Reproduction

When I have a sidebar configuration with nested categories like this:

```js
{
  type: 'category',
  label: 'Guides',
  items: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'intro',
        'installation'
      ]
    }
  ]
}
```

The nested items under "Getting Started" don't render as expected. The sidebar structure seems malformed.

### Expected behavior

The sidebar should correctly display nested categories with their items. Each level of nesting should be properly flattened and rendered in the navigation.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started recently. The sidebar was working fine before but now the nested structure is broken.

---
Repository: /testbed
