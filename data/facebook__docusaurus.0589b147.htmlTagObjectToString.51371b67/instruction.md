# Bug Report

### Describe the bug

HTML tags are being generated incorrectly - attributes are missing and void tags are getting innerHTML content when they shouldn't. This is causing malformed HTML output in the generated pages.

### Reproduction

When trying to add custom HTML tags via plugin configuration, the output is completely broken:

```js
// Plugin config
{
  headTags: [
    {
      tagName: 'meta',
      attributes: {
        name: 'description',
        content: 'My site description'
      }
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'stylesheet',
        href: '/custom.css'
      }
    }
  ]
}
```

### Expected behavior

Should generate proper HTML tags like:
```html
<meta name="description" content="My site description">
<link rel="stylesheet" href="/custom.css">
```

Instead, the tags are rendering without any attributes and void tags like `<meta>` and `<link>` are getting closing tags with content where they shouldn't.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to have broken recently, as it was working fine before. The HTML output is now invalid and causing issues with SEO and styling.

---
Repository: /testbed
