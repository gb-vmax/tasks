# Bug Report

### Describe the bug

I'm encountering an issue with MDX compilation where JSX elements with a single child are not being rendered correctly. The child element seems to be getting dropped during the compilation process.

### Reproduction

```jsx
// Input MDX
<div>
  <span>Single child element</span>
</div>

// Expected output: div with span child
// Actual output: div without children
```

When I have a JSX element with exactly one child, the child doesn't appear in the compiled output. Elements with zero children or multiple children seem to work fine, but single-child elements are broken.

### Expected behavior

JSX elements with a single child should render that child correctly, just like elements with multiple children do.

### Additional context

This seems to have started happening recently. I noticed that:
- Empty elements (no children) work fine
- Elements with 2+ children work fine  
- Elements with exactly 1 child lose that child

Not sure if this is related to how the children array is being processed during compilation.

---
Repository: /testbed
