# Bug Report

### Describe the bug

The redirect plugin is now overwriting existing files instead of preventing file overrides as intended. It seems like the safety check that was supposed to protect existing files from being overwritten is no longer working correctly.

### Reproduction

1. Create a static file at a specific path (e.g., `build/some-page/index.html`)
2. Configure a redirect that would write to the same path
3. Run the build process
4. The existing file gets overwritten instead of throwing an error

Expected: The plugin should throw an error saying "The redirect plugin is not supposed to override existing files."

Actual: The existing file is silently overwritten by the redirect file.

### Expected behavior

The plugin should detect when a redirect would overwrite an existing file and throw an error to prevent data loss. This is a safety feature to avoid accidentally replacing real content with redirect files.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This is a pretty serious issue since it could lead to content being accidentally deleted during builds. Would appreciate a fix soon!

---
Repository: /testbed
