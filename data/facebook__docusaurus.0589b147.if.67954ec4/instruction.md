# Bug Report

### Describe the bug

I'm experiencing an issue with document navigation links in the docs plugin. When a document has an empty string (`''`) as the navigation link ID (either for `prev` or `next`), the navigation link is not being handled correctly. Instead of treating the empty string as "no navigation link", it seems to be processed further, which causes unexpected behavior.

### Reproduction

In your document's front matter, set the previous or next navigation to an empty string:

```yaml
---
id: my-doc
sidebar_label: My Document
pagination_prev: ''
---
```

Or programmatically:

```js
const navLink = {
  prev: '',
  next: 'some-other-doc'
}
```

### Expected behavior

When `pagination_prev` or `pagination_next` is set to an empty string, it should be treated the same as if it were `null` or `undefined` - meaning no navigation link should be rendered for that direction. The navigation component should gracefully handle empty strings and not attempt to look up a document with an empty ID.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
