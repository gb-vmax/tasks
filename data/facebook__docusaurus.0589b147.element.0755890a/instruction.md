# Bug Report

### Describe the bug

After a recent update, inline styles are not being applied correctly to JSX elements in MDX files. The style attribute seems to be completely ignored when rendering components.

### Reproduction

```jsx
// In an MDX file
<div style={{ color: 'red', fontSize: '16px' }}>
  This text should be red
</div>

// Or using string styles
<p style="background: blue; padding: 10px">
  This should have a blue background
</p>
```

The elements render without any inline styles applied. The style attribute appears to be skipped during the transformation process.

### Expected behavior

Inline styles defined via the `style` attribute should be properly applied to the rendered elements. Both object notation and string notation for styles should work as expected.

### Additional context

This seems to have started happening recently. Other attributes like `className`, `id`, etc. are working fine - it's specifically the `style` attribute that's not being processed correctly.

---
Repository: /testbed
