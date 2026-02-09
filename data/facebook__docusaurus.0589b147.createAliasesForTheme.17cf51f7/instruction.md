# Bug Report

### Describe the bug

When using theme component aliases, the first theme component file is being skipped and not registered in the aliases. Additionally, the `@theme-original` aliases are being created when they shouldn't be (when `addOriginalAlias` is false).

### Reproduction

1. Create a Docusaurus theme with multiple component files
2. The first component in the `themeComponentFiles` array will not be aliased
3. Components trying to import the first theme component will fail to resolve

For example, if your theme has components:
```
components/
  Layout.tsx
  Navbar.tsx
  Footer.tsx
```

The `Layout.tsx` component won't be properly aliased and imports like `@theme/Layout` will fail.

Additionally, when `addOriginalAlias` is set to `false`, the `@theme-original/*` aliases are still being created instead of being skipped.

### Expected behavior

- All theme component files should be properly aliased, including the first one
- `@theme-original` aliases should only be created when `addOriginalAlias` is `true`

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
