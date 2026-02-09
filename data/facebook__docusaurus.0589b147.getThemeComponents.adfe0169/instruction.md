# Bug Report

### Describe the bug

When trying to swizzle components, the component ordering seems incorrect. Components that should be marked as safe are not appearing first in the list, and some components that should be available for swizzling are being filtered out incorrectly.

### Reproduction

1. Run the swizzle command to list available components
2. Notice that the component list ordering doesn't prioritize safe components
3. Try to swizzle a component that should be available but isn't showing up in the list

The filtering logic appears to be too strict - components that exist in the theme are being excluded from the available components list even though they should be swizzleable.

### Expected behavior

- Safe components (those with safe wrap/eject actions) should appear at the top of the list
- All valid theme components should be available for swizzling
- The component list should be properly ordered by safety level

### Additional context

This affects the developer experience when using the swizzle command, as it's harder to find the components you want to customize and some valid components may not be accessible at all.

---
Repository: /testbed
