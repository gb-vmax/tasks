# Bug Report

### Describe the bug

I'm encountering an issue where using the legacy `author_*` front matter fields in blog posts is now throwing an error even when I'm not mixing them with the new `authors` field. This seems to have broken backward compatibility.

### Reproduction

Create a blog post with only legacy author fields:

```md
---
title: My Blog Post
author: John Doe
author_title: Software Engineer
author_url: https://example.com
author_image_url: https://example.com/avatar.jpg
---

Post content here...
```

When building the site, I get this error:

```
Error: To declare blog post authors, use the 'authors' front matter in priority.
Don't mix 'authors' with other existing 'author_*' front matter. Choose one or the other, not both at the same time.
```

### Expected behavior

The legacy `author_*` fields should continue to work on their own without throwing an error. The error should only appear when actually mixing the old and new formats together (e.g., having both `authors` and `author_*` fields in the same post).

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is blocking our migration as we have many existing blog posts using the legacy format. Any help would be appreciated!

---
Repository: /testbed
