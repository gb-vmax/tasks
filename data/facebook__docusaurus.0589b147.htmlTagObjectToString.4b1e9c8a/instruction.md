# Bug Report

### Describe the bug

HTML tags are being rendered incorrectly - void tags (like `<meta>`, `<link>`, `<img>`) are getting closing tags when they shouldn't, and non-void tags are missing their closing tags.

### Reproduction

When adding custom HTML tags through the plugin system:

```js
// In docusaurus.config.js
module.exports = {
  // ...
  headTags: [
    {
      tagName: 'link',
      attributes: {
        rel: 'stylesheet',
        href: '/custom.css',
      },
    },
    {
      tagName: 'div',
      innerHTML: 'Some content',
    },
  ],
};
```

The output HTML is malformed:
- `<link>` tags get closing `</link>` tags (they shouldn't)
- `<div>` tags don't get closing `</div>` tags (they should)

### Expected behavior

Void tags like `<link>`, `<meta>`, `<img>`, etc. should be self-closing and not have closing tags.
Non-void tags should have proper closing tags when they contain content.

Expected output:
```html
<link rel="stylesheet" href="/custom.css">
<div>Some content</div>
```

This seems to have broken recently and is causing invalid HTML to be generated.

---
Repository: /testbed
