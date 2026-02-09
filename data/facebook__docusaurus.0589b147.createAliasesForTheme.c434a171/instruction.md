# Bug Report

### Describe the bug

I'm experiencing an issue with theme component aliases in Docusaurus. When I try to use custom theme components, the aliases don't seem to be resolving correctly. The `@theme` imports are not working as expected, and I'm getting module resolution errors.

### Reproduction

```js
// In a custom theme component
import Layout from '@theme/Layout';
import Navbar from '@theme/Navbar';

// These imports fail to resolve correctly
```

Steps to reproduce:
1. Create a custom theme with multiple components
2. Try to import components using `@theme` alias
3. The imports don't resolve to the correct file paths

### Expected behavior

The `@theme` alias should correctly map to the theme component files, allowing imports like `@theme/Layout` to resolve to the actual component file path.

### Additional context

This seems to affect the webpack alias configuration for theme components. The issue appears when setting up theme aliases, where the mapping between the alias names and actual file paths isn't being created properly.

---
Repository: /testbed
