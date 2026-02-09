# Bug Report

### Describe the bug

The navbar logo alt text is not being translated correctly. When I set up translations for my navbar logo using the `logo.alt` translation key, it doesn't apply - the logo just shows the default alt text instead of the translated version.

Also noticed that dropdown menu items in the navbar are completely disappearing. I have a navbar item with subitems configured, but none of the subitems are rendering in the UI anymore.

### Reproduction

1. Configure a navbar with a logo and alt text in `docusaurus.config.js`:
```js
navbar: {
  logo: {
    alt: 'My Site Logo',
    src: 'img/logo.svg',
  },
}
```

2. Add a translation for the logo alt text in your translation files:
```json
{
  "theme.navbar.logo.alt": {
    "message": "Translated Logo Text"
  }
}
```

3. The logo still shows "My Site Logo" instead of "Translated Logo Text"

For the dropdown items issue:
1. Configure a navbar item with subitems:
```js
navbar: {
  items: [
    {
      label: 'Docs',
      items: [
        { label: 'Getting Started', to: '/docs/intro' },
        { label: 'API', to: '/docs/api' }
      ]
    }
  ]
}
```

2. The dropdown menu appears empty - no subitems are shown

### Expected behavior

- Logo alt text should use the translated message when available
- All navbar dropdown subitems should be visible and functional

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
