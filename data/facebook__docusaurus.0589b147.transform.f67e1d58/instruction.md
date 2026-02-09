# Bug Report

### Describe the bug

I'm encountering an issue with ARIA attribute transformation in MDX. When using ARIA properties in JSX, they're not being converted to the correct attribute names. Specifically, the `role` attribute seems to be affected, and other ARIA attributes are being incorrectly transformed.

### Reproduction

```jsx
<div ariaLabel="Navigation menu" role="navigation">
  Content here
</div>
```

When this gets processed, the ARIA attributes don't get transformed properly. The `role` attribute should remain as `role`, but other ARIA properties like `ariaLabel` should be converted to `aria-label`.

### Expected behavior

- `role` should stay as `role` (not transformed)
- `ariaLabel` should be transformed to `aria-label`
- `ariaActiveDescendant` should be transformed to `aria-activedescendant`
- Other ARIA properties should follow the same pattern: `aria-` prefix + lowercase conversion

### Current behavior

The transformation logic appears to be inverted or incorrect, causing ARIA attributes to not render properly in the final output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
