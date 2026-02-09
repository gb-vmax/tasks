# Bug Report

### Describe the bug

Footer translations are not working correctly. The translation keys for footer link titles and items appear to be swapped, causing translations to fail to load properly. Additionally, the logo alt text fallback is using the wrong property.

### Reproduction

```js
// docusaurus.config.js
footer: {
  links: [
    {
      title: 'Docs',
      items: [
        {
          label: 'Tutorial',
          to: '/docs/intro',
        },
      ],
    },
  ],
  logo: {
    alt: 'My Site Logo',
    src: 'img/logo.svg',
  },
}
```

```json
// i18n/en/docusaurus-theme-classic/footer.json
{
  "link.title.Docs": {
    "message": "Documentation"
  },
  "link.item.label.Tutorial": {
    "message": "Getting Started"
  },
  "logo.alt": {
    "message": "Company Logo"
  }
}
```

### Expected behavior

- Footer link titles should use the `link.title.*` translation key
- Footer link item labels should use the `link.item.label.*` translation key  
- Logo alt text should fallback to the original `alt` property, not `src`

### Actual behavior

- Footer link titles are looking for `link.item.label.*` keys instead
- Footer link item labels are looking for `link.title.*` keys instead
- Logo alt text falls back to the image source path when translation is missing

This means the translations don't get applied and you end up with either the original text or incorrect fallback values.

---
Repository: /testbed
