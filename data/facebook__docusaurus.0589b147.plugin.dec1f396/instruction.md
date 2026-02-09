# Bug Report

### Describe the bug

The MDX loader is incorrectly transforming `<details>` elements in markdown. It appears that `<details>` tags are being renamed to `<Details>` when they shouldn't be, or the transformation logic is inverted.

### Reproduction

```mdx
<details>
<summary>Click to expand</summary>

Some hidden content here

</details>
```

When processing this MDX content, the `<details>` element gets incorrectly transformed. The element name is being changed when it should remain as `details`, breaking the native HTML functionality.

### Expected behavior

The `<details>` HTML element should be transformed to `<Details>` (capitalized) for React component handling, but instead the transformation logic seems backwards - it's transforming everything that is NOT a details element.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This is causing issues with collapsible sections in documentation not working as expected.

---
Repository: /testbed
