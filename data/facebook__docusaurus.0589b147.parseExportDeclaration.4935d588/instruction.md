# Bug Report

### Describe the bug

I'm encountering an issue with export declarations in MDX files. After a recent update, it seems like export statements are being parsed incorrectly, which is causing problems when trying to use standard JavaScript export syntax in MDX documents.

### Reproduction

```mdx
export const metadata = {
  title: 'My Page',
  description: 'Page description'
}

# My Content

Some MDX content here...
```

When trying to use this pattern, the export declaration doesn't seem to be handled properly. The parser appears to be treating it differently than expected.

### Expected behavior

Export declarations should be parsed as statements, allowing for standard JavaScript export syntax to work correctly in MDX files. This pattern has been working fine in previous versions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
