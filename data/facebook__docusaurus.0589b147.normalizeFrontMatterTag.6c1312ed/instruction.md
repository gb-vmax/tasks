# Bug Report

### Describe the bug

When using custom tag permalinks in front matter, the permalink is not being used correctly. Instead of using the specified permalink value, the system appears to be using the tag label to generate the permalink path.

### Reproduction

```yaml
---
tags:
  - label: 'My Custom Tag'
    permalink: '/custom-path'
---
```

After setting up a tag with a custom permalink like above, the generated tag page URL doesn't use the custom permalink. The tag page is created at a path based on the label instead of respecting the `permalink` field.

### Expected behavior

When a tag object includes a custom `permalink` field, that permalink should be used for the tag page URL. The `permalink` property should take precedence over the auto-generated one from the label.

For example, with the config above, I would expect the tag page to be accessible at `/tags/custom-path` (or similar, depending on tagsPath), not at a URL derived from "My Custom Tag".

### Additional context

This seems to affect any tags defined as objects with custom permalinks in the front matter. Tags defined as simple strings work fine with auto-generated permalinks.

---
Repository: /testbed
