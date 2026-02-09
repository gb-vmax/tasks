# Bug Report

### Describe the bug

I'm encountering an issue with slug generation for docs when using front matter slugs that start with a forward slash. It seems like the slug handling logic is inverted - slugs starting with `/` are being processed incorrectly and having characters removed from them.

### Reproduction

Create a doc file with a front matter slug that starts with `/`:

```md
---
slug: /my-custom-slug
---

# My Doc
```

When this doc is processed, the slug gets mangled. It appears that absolute slugs (those starting with `/`) are not being handled as absolute paths anymore.

### Expected behavior

When I specify a slug starting with `/` in the front matter, it should be treated as an absolute slug path and used as-is. The leading slash should be preserved and the slug should not have any characters stripped from it.

Currently it seems like the logic is backwards - slugs WITH a leading slash are being modified when they shouldn't be.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
