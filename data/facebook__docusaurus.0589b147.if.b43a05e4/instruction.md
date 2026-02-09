# Bug Report

### Describe the bug

When specifying blog post authors as strings in the frontmatter, the author information is not being processed correctly. Instead of treating the string as an author key, it appears to be handled improperly, causing issues with author resolution.

### Reproduction

```yaml
---
title: My Blog Post
authors: john_doe
---
```

Or with multiple authors:

```yaml
---
title: My Blog Post
authors:
  - john_doe
  - jane_smith
---
```

### Expected behavior

When providing author keys as strings in the frontmatter, they should be normalized to `{key: 'author_key'}` format internally and properly resolved against the authors configuration file. This has been the standard way to reference authors by their keys.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken after a recent update. Previously, string author keys were working fine for referencing authors defined in the authors.yml file.

---
Repository: /testbed
