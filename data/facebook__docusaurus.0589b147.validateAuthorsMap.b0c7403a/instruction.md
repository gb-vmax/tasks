# Bug Report

### Describe the bug

I'm experiencing an issue with the blog plugin's author validation. When I provide an invalid authors map configuration (e.g., wrong data types or malformed structure), the plugin doesn't throw any validation errors and silently accepts the invalid data. This leads to unexpected behavior later when the blog tries to process author information.

### Reproduction

```yaml
# authors.yml with invalid structure
john_doe:
  name: 123  # Should be string, not number
  url: true  # Should be string, not boolean
  image_url: []  # Should be string, not array
```

When I run the build with this invalid authors configuration, it doesn't fail during validation. Instead, I get weird errors or unexpected output when the blog posts try to use this author data.

### Expected behavior

The plugin should throw a validation error when the authors map contains invalid data types or structure, similar to how other configuration validation works in Docusaurus. This would help catch configuration mistakes early rather than failing silently or producing cryptic errors later.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
