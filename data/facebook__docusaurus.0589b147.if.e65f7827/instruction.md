# Bug Report

### Describe the bug

When specifying blog post authors as strings in the front matter, they are no longer being recognized correctly. The author information doesn't appear in the rendered blog post.

### Reproduction

Create a blog post with a string author reference:

```md
---
title: My Blog Post
authors: john_doe
---

Post content here...
```

Or with multiple authors:

```md
---
title: My Blog Post
authors: [john_doe, jane_smith]
---

Post content here...
```

Where `john_doe` and `jane_smith` are defined in the authors configuration file.

### Expected behavior

The blog post should display the author information by looking up the author key in the configured authors map. String keys should be resolved to their corresponding author objects.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This was working fine before but seems to have broken recently. The authors just don't show up anymore when using string keys.

---
Repository: /testbed
