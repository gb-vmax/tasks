# Bug Report

### Describe the bug

When using the blog plugin with an `authors.yml` file, I'm encountering a strange issue where invalid author configurations are being accepted without any validation errors. The plugin seems to be allowing malformed author data through, which then causes problems downstream.

### Reproduction

Create an `authors.yml` file with invalid data:

```yaml
john_doe:
  name: 123  # should be a string
  url: not-a-valid-url
  image_url: []  # should be a string
```

Expected: The build should fail with a validation error
Actual: The build succeeds and uses the invalid data

### Steps to reproduce

1. Set up a Docusaurus blog with the blog plugin
2. Create an `authors.yml` file with invalid author data (wrong types, missing required fields, etc.)
3. Reference the author in a blog post
4. Run the build

The build completes successfully even though the author data is clearly invalid. This is problematic because it allows bad data to slip through that should be caught during validation.

### Expected behavior

The plugin should validate the authors map and throw an error when the data doesn't match the expected schema. Invalid configurations should be rejected during the build process.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
