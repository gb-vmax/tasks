# Bug Report

### Describe the bug

I'm experiencing an issue with blog post tag visibility when using unlisted posts. Tags that should be hidden (because all their posts are unlisted) are still showing up as visible in the tag list.

### Reproduction

```js
// Create a blog post with unlisted: false
const post1 = {
  metadata: {
    unlisted: false,
    tags: ['tutorial']
  }
}

// Create a blog post with unlisted: true
const post2 = {
  metadata: {
    unlisted: true,
    tags: ['tutorial']
  }
}
```

When a tag only has unlisted posts, it should be marked as unlisted/hidden, but instead it's being treated as visible. The tag visibility calculation seems to be checking for the presence of the `unlisted` property rather than its actual boolean value.

### Expected behavior

Tags should only be visible if they have at least one post where `unlisted` is explicitly `false`. If all posts under a tag have `unlisted: true`, the tag itself should be unlisted.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-blog

---
Repository: /testbed
