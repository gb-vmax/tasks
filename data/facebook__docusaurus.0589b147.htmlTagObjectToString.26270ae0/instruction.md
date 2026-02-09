# Bug Report

### Describe the bug

HTML tags are not rendering correctly when using `htmlTagObjectToString`. Attributes are being stripped from tags and self-closing tags are showing unexpected content.

### Reproduction

```js
const tag = {
  tagName: 'meta',
  attributes: {
    name: 'description',
    content: 'My site description'
  }
};

// Result: <meta> instead of <meta name="description" content="My site description">
const result = htmlTagObjectToString(tag);
```

Also seeing issues with void tags (like `<img>`, `<br>`, `<meta>`) that should be self-closing but are rendering with innerHTML when they shouldn't have any content.

### Expected behavior

- Tags should include all their attributes in the output
- Void/self-closing tags should not render innerHTML even if accidentally provided
- Normal tags should only render innerHTML when explicitly set (not undefined/null)

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
