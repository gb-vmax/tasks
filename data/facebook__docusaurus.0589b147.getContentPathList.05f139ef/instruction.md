# Bug Report

### Describe the bug

I'm experiencing an issue with content path resolution in the pages plugin. When the localized content path is the same as the base content path, it appears that files are being processed twice, leading to duplicate content or unexpected behavior.

### Reproduction

This happens when:
1. The `contentPathLocalized` and `contentPath` are identical (e.g., both pointing to the same directory)
2. The plugin processes the content paths
3. Files from that directory get loaded/processed multiple times

For example, in a non-localized setup or when the default locale matches the content path:
```js
{
  contentPath: 'src/pages',
  contentPathLocalized: 'src/pages'  // Same as contentPath
}
```

The current behavior seems to include both paths in the list even when they're identical, which causes the same files to be read twice.

### Expected behavior

When `contentPathLocalized` and `contentPath` point to the same directory, the path should only be included once in the content path list to avoid duplicate processing.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
