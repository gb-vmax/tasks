# Bug Report

### Describe the bug

I'm experiencing an issue with tag permalink generation in Docusaurus. When using custom tag objects (not just strings) in frontmatter, the permalink is being set to the tag label instead of being properly normalized with the tags path.

### Reproduction

```yaml
---
tags:
  - label: "My Tag"
    permalink: "custom-permalink"
---
```

After this change, the tag permalink ends up as just `"My Tag"` instead of the expected normalized path like `/tags/custom-permalink`.

### Expected behavior

When providing a custom permalink in a tag object, it should be normalized with the tags path (e.g., `/tags/custom-permalink`), not replaced with the raw label value.

For string tags, the behavior seems fine - they get converted to kebab-case and normalized properly. But for object-style tags with custom permalinks, the normalization is being skipped entirely.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
