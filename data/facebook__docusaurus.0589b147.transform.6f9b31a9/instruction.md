# Bug Report

### Describe the bug

I'm experiencing an issue with ARIA attribute transformation in MDX. When using ARIA properties like `ariaLabel`, `ariaDescribedBy`, etc., they're not being converted to the correct attribute names in the rendered output.

### Reproduction

```jsx
<div ariaLabel="test" role="button">
  Content
</div>
```

When this gets rendered, the ARIA attributes aren't being properly transformed. It seems like the property names are being passed through incorrectly instead of being converted to their hyphenated `aria-*` equivalents.

### Expected behavior

ARIA properties should be transformed to their correct attribute names:
- `ariaLabel` → `aria-label`
- `ariaDescribedBy` → `aria-describedby`
- `ariaHidden` → `aria-hidden`
- etc.

The `role` attribute should remain as `role` (not transformed).

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
