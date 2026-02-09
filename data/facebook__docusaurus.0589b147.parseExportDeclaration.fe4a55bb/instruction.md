# Bug Report

### Describe the bug

I'm experiencing an issue with MDX export declarations where the parser seems to be processing statements incorrectly. When using export declarations in my MDX files, the exported values are getting lost or corrupted during parsing.

### Reproduction

```mdx
export const metadata = {
  title: 'My Document',
  author: 'John Doe'
}

# My Content

This is my MDX document.
```

When this MDX file is parsed, the export declaration doesn't work as expected. The metadata object is not properly exported and becomes inaccessible to consuming components.

### Expected behavior

The export statement should be parsed correctly and the exported values should be available for use. The metadata object should be accessible after parsing the MDX file.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
