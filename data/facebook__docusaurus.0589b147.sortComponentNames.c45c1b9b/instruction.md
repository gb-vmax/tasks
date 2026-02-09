# Bug Report

### Describe the bug

After updating, some components are missing from the swizzle command output. When I run the swizzle command to see available components, certain components that should be listed are not showing up anymore.

### Reproduction

```bash
# Run swizzle command to list components
npm run swizzle -- --list

# Expected: All theme components should be listed
# Actual: Some components with certain naming patterns are missing
```

For example, components like `NavBarItem`, `SearchBar`, or `BlogPostItem` might not appear in the list even though they exist in the theme.

### Expected behavior

All available theme components should be displayed when listing swizzleable components, regardless of their naming convention. Components with uppercase letters in the middle of their names should still be included in the output.

### Additional context

This seems to affect components that have camelCase or PascalCase naming patterns with uppercase letters in the middle positions. The swizzle list used to show all components but now filters some out unexpectedly.

---
Repository: /testbed
