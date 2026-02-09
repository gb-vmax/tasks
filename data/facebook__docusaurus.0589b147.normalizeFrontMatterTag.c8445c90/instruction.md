# Bug Report

### Describe the bug

When using custom tag permalinks in front matter, the permalink property is being ignored and the tag label is used instead. This breaks existing documentation that relies on custom permalinks for tags.

### Reproduction

```yaml
---
tags:
  - label: 'My Tag'
    permalink: '/custom-permalink'
---
```

After processing, the tag permalink becomes `/tags/My Tag` instead of the expected `/tags/custom-permalink`.

### Expected behavior

When a tag object with both `label` and `permalink` properties is provided in front matter, the custom permalink should be preserved and used. The tag should be created with:
- label: 'My Tag'
- permalink: '/tags/custom-permalink'

### Additional context

This appears to be a regression. Previously, tags could have custom permalinks that differed from their labels, which was useful for:
- Creating cleaner URLs
- Maintaining backwards compatibility when renaming tags
- Handling special characters in tag labels

Now all tags are forced to use their label as the permalink, regardless of what's specified in the front matter.

---
Repository: /testbed
