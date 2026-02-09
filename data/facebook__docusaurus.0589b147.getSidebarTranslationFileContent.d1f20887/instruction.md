# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar translations in the docs plugin. It seems like the translation extraction is not working correctly - some sidebar items that should be translatable are being excluded, while others that shouldn't be translatable are being included.

### Reproduction

When I run the translation extraction for my docs sidebar, I'm seeing unexpected behavior:

1. Sidebar categories with `generated-index` links are not getting their title/description extracted for translation
2. Sidebar doc items that are marked as non-translatable are still appearing in the translation files

Here's my sidebar config:

```js
{
  type: 'category',
  label: 'Getting Started',
  link: {
    type: 'generated-index',
    title: 'Welcome to Our Docs',
    description: 'This is the introduction page'
  },
  items: [...]
}
```

### Expected behavior

- Categories with `generated-index` links should have their title and description extracted to translation files
- Only translatable doc items should appear in the translation output
- Non-translatable items (those explicitly marked as `translatable: false`) should be excluded

### System Info

- Docusaurus version: latest
- Node version: 18.x

This is blocking our i18n implementation, so any help would be appreciated!

---
Repository: /testbed
