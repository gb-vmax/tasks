# Bug Report

### Describe the bug

I'm experiencing an issue with HTML tag rendering where void/self-closing tags are being rendered with closing tags when they shouldn't have them. Tags like `<meta>`, `<link>`, `<img>`, etc. are being generated with closing tags like `</meta>`, `</link>`, which is invalid HTML.

### Reproduction

When generating HTML tags programmatically, void elements are incorrectly rendered:

```js
// Example: meta tag
const metaTag = {
  tagName: 'meta',
  attributes: {
    name: 'description',
    content: 'My site'
  }
}

// Current output: <meta name="description" content="My site"></meta>
// Expected output: <meta name="description" content="My site">
```

Similar issue occurs with other void elements like `<link>`, `<img>`, `<br>`, `<hr>`, etc.

### Expected behavior

Void/self-closing HTML elements should not have closing tags. According to HTML5 spec, elements like `meta`, `link`, `img`, `br`, `hr`, `input`, etc. should not have closing tags.

Expected:
- `<meta name="description" content="test">`
- `<link rel="stylesheet" href="style.css">`
- `<img src="image.png" alt="test">`

Not:
- `<meta name="description" content="test"></meta>`
- `<link rel="stylesheet" href="style.css"></link>`
- `<img src="image.png" alt="test"></img>`

### Additional context

This appears to affect the HTML tag generation logic and results in invalid HTML being produced for void elements.

---
Repository: /testbed
