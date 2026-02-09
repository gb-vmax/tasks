# Bug Report

### Describe the bug

When building docs with tags, the tags list page is not being generated correctly. Instead of showing the tags list when tags exist, an empty object is being returned, which causes the route to fail to render properly.

### Reproduction

1. Create a docs version with multiple tagged pages
2. Build the documentation
3. Navigate to the tags list page (e.g., `/docs/tags`)
4. The page fails to load or shows unexpected behavior

Example configuration:
```js
// In your docs with tags
---
tags:
  - guide
  - tutorial
---
```

When you have tags defined across your documentation, the tags list route should be created, but instead it's returning an empty object when tags are present.

### Expected behavior

The tags list page should be generated and display all available tags when there are tags in the documentation. The route should only return `null` when there are no tags to display.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
