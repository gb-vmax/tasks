# Bug Report

### Describe the bug

After a recent update, MDX heading IDs and admonitions are being processed incorrectly. Heading IDs that should be escaped are not being escaped, and admonition titles are being converted to directive labels even when they shouldn't be.

### Reproduction

When using MDX files with the following configuration:

```js
{
  markdownConfig: {
    mdx1Compat: {
      headingIds: true,
      admonitions: true
    }
  }
}
```

**Case 1: Heading IDs**
Input MDX:
```md
## My Heading {#custom-id}
```

Expected: The heading ID should be preserved as-is when `mdx1Compat.headingIds` is `true`
Actual: The heading ID gets escaped even though compatibility mode is enabled

**Case 2: Admonitions**
Input MDX:
```md
:::note Title
Content here
:::
```

Expected: Admonition title should remain unchanged when `mdx1Compat.admonitions` is `true`
Actual: The title gets converted to directive label format even with compatibility mode enabled

### Expected behavior

When `mdx1Compat.headingIds` is set to `true`, heading IDs should NOT be escaped (maintaining MDX v1 compatibility).
When `mdx1Compat.admonitions` is set to `true`, admonition titles should NOT be converted to directive labels (maintaining MDX v1 compatibility).

The compatibility flags seem to be having the opposite effect of what they should do.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
