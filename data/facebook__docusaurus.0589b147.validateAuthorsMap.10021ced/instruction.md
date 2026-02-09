# Bug Report

### Describe the bug

I'm encountering an issue with the blog plugin's authors validation. When I provide a valid `authors.yml` file, the build process throws an error and fails. Conversely, when I intentionally provide an invalid authors configuration, the build succeeds without any validation errors.

### Reproduction

Create an `authors.yml` file with valid author data:

```yaml
john_doe:
  name: John Doe
  title: Software Engineer
  url: https://github.com/johndoe
  image_url: https://github.com/johndoe.png
```

When building the site with this valid configuration, I get an error thrown during the validation step. However, if I provide invalid data (like missing required fields or incorrect types), the build completes successfully without any warnings.

### Expected behavior

- Valid author configurations should pass validation and build successfully
- Invalid author configurations should fail validation and throw appropriate errors
- The validation should work as intended to catch malformed author data

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like the validation logic might be inverted somehow. The behavior is completely opposite of what it should be.

---
Repository: /testbed
