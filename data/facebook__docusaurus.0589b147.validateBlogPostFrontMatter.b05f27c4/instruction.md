# Bug Report

### Describe the bug

I'm experiencing an issue with blog post tags where the first tag is being removed unexpectedly. When I define tags in the front matter of my blog posts, only tags from the second position onwards are appearing in the final output.

### Reproduction

Create a blog post with the following front matter:

```md
---
title: My Blog Post
tags: [javascript, react, webdev, tutorial]
---

Blog content here...
```

**Expected tags:** `['javascript', 'react', 'webdev', 'tutorial']`
**Actual tags:** `['react', 'webdev', 'tutorial']`

The first tag (`javascript`) is missing from the rendered post.

### Expected behavior

All tags defined in the front matter should be preserved and displayed. The tags array should not have any elements removed during processing.

### Additional context

This seems to have started happening recently. I have multiple blog posts affected by this issue, and in all cases the first tag is being dropped. Not sure if this is related to front matter validation or some other processing step.

---
Repository: /testbed
