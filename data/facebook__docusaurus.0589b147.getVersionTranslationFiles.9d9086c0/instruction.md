# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where the translation files are not being generated correctly. After a recent update, the version translation files seem to be missing or malformed, which is breaking the i18n functionality for versioned docs.

### Reproduction

1. Set up a Docusaurus site with versioned docs
2. Enable i18n with multiple locales
3. Try to generate translation files for a specific version
4. The translation file structure is incorrect - instead of getting the expected translation file object with `path` and `content`, I'm getting just the content directly

Expected structure:
```js
[
  {
    path: 'version-1.0.0.json',
    content: { /* translations */ }
  }
]
```

What I'm actually getting appears to be just the content without the wrapper object.

### Expected behavior

The translation files should maintain their proper structure with both `path` and `content` properties so that the i18n system can correctly write the files to disk.

### System Info

- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
