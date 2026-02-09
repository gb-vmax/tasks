# Bug Report

### Describe the bug

I'm experiencing an issue with navbar translation file generation where nested navigation items cause an infinite loop. When I have a navbar configuration with nested items (dropdown menus), the site build hangs indefinitely and never completes.

### Reproduction

Set up a navbar configuration with nested items:

```js
navbar: {
  items: [
    {
      label: 'Docs',
      items: [
        {
          label: 'Getting Started',
          to: '/docs/intro'
        },
        {
          label: 'API',
          to: '/docs/api'
        }
      ]
    }
  ]
}
```

When the translation file is being generated, the build process hangs and never completes. I have to manually kill the process.

### Expected behavior

The navbar translation file should be generated successfully even with nested navigation items, and the build should complete normally.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. My navbar config hasn't changed but builds that used to work are now hanging.

---
Repository: /testbed
