# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM data parsing where the order of operations seems incorrect. When processing MDX files with ESM imports/exports, the data handling appears to be reversed, causing unexpected behavior in the parsed output.

### Reproduction

```mdx
export const metadata = {
  title: 'Test Page',
  description: 'A test page'
}

# My Content

Some content here
```

When parsing this MDX file, the ESM data tokens are being processed in the wrong sequence, which affects how the metadata is extracted and made available to the component.

### Expected behavior

The ESM export data should be properly parsed and the metadata should be accessible in the correct order. The enter/exit handlers for data tokens should be called in the proper sequence to maintain the integrity of the parsed content.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have broken after a recent update. The parsing logic for ESM blocks doesn't seem to be handling the token data correctly anymore.

---
Repository: /testbed
