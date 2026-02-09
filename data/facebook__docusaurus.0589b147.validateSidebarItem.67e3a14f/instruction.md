# Bug Report

### Describe the bug

I'm encountering an issue with sidebar validation in the docs plugin. When I have a sidebar item with type `'doc'` or `'ref'` (basically any non-link type), the validation logic tries to access an `items` property that doesn't exist, which causes a runtime error.

### Reproduction

```js
const sidebar = {
  docs: [
    {
      type: 'doc',
      id: 'intro',
      label: 'Introduction'
    }
  ]
}
```

When this sidebar configuration is processed, the validation fails because the code attempts to call `.map()` on `items` property of a doc-type sidebar item, but doc items don't have an `items` property - only category items do.

### Expected behavior

The validation should only process the `items` array for sidebar items of type `'category'`, since other item types (like `'doc'`, `'ref'`, etc.) don't have nested items.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
