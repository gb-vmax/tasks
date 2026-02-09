# Bug Report

### Describe the bug

The swizzle command is showing components in the wrong order. Instead of showing the safest components first (those that can be safely wrapped/ejected), it's now showing them last. This makes it harder to find the recommended components to swizzle.

Also, intermediate folders (folders without an index component) are being treated as regular components and showing incorrect swizzle actions available.

### Reproduction

```bash
# Run the swizzle command in a Docusaurus project
docusaurus swizzle

# The component list appears in reverse order - unsafe components are shown first
# Intermediate folders are incorrectly marked as swizzleable
```

### Expected behavior

- Components should be ordered with the safest ones first (those that support both wrap and eject actions)
- Intermediate folders should be properly identified and excluded from wrapping
- The component list should prioritize showing components that are safe to swizzle

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
