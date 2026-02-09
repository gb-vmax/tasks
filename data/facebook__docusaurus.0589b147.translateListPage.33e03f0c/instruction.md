# Bug Report

### Describe the bug

After a recent update, the blog list pagination structure seems to be broken. The `items` array that should contain the blog posts is now nested inside the `metadata` object instead of being at the top level of the page object.

### Reproduction

When accessing a paginated blog list page, the structure returned is:

```js
{
  metadata: {
    items: [...], // posts are here now
    blogTitle: "...",
    blogDescription: "...",
    // other metadata fields
  }
}
```

But it should be:

```js
{
  items: [...], // posts should be here
  metadata: {
    blogTitle: "...",
    blogDescription: "...",
    // other metadata fields
  }
}
```

This breaks any code that tries to access `page.items` directly, as the items are now incorrectly placed inside the metadata object.

### Expected behavior

The `items` array should be a top-level property of each page object, not nested inside `metadata`. The blog list pagination should maintain the correct structure with items and metadata as separate top-level properties.

### System Info
- Docusaurus plugin: @docusaurus/plugin-content-blog

---
Repository: /testbed
