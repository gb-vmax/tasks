# Bug Report

### Describe the bug

I'm experiencing an issue with tag visibility in blog posts. When working with blog tags, the visibility calculation seems to be inverted or broken. Tags that should be visible are being marked as unlisted, and vice versa.

### Reproduction

```js
const blogPost = {
  metadata: {
    unlisted: false
  }
}

// Tag visibility is calculated incorrectly
// Posts with unlisted: false are being treated as unlisted
```

### Expected behavior

Blog tags should correctly determine visibility based on the `unlisted` property in the post metadata. If a post has `metadata.unlisted: false`, the tag should be visible. If `metadata.unlisted: true`, the tag should be unlisted.

Currently, it seems like the logic is backwards - posts that are NOT unlisted are being treated as if they ARE unlisted.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-blog

---
Repository: /testbed
