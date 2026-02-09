# Bug Report

### Describe the bug

After a recent update, the `@theme-original` aliases are being created when they shouldn't be, and the `@theme` aliases are using the wrong path. This is causing issues with theme component resolution in Docusaurus.

### Reproduction

When creating theme aliases with `addOriginalAlias` set to `false`:

1. Create a theme component with a nested directory structure (e.g., `components/Button/index.tsx`)
2. The `@theme` alias is created using the full relative path instead of the converted file path
3. The `@theme-original` alias is created even though `addOriginalAlias` is `false`

### Expected behavior

- When `addOriginalAlias` is `false`, the `@theme-original` aliases should NOT be created
- The `@theme` alias should use the converted `fileName` (from `fileToPath()`) not the raw `relativeSource`

For example, with a file at `components/Button/index.tsx`:
- `@theme` should map to `@theme/components/Button` (using fileName)
- `@theme-original` should only exist when `addOriginalAlias` is `true`

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like the condition logic got inverted and the wrong variable is being used for the alias name.

---
Repository: /testbed
