# Bug Report

### Describe the bug

Theme aliases are not being generated correctly. When trying to use `@theme` imports in my components, the paths are resolving incorrectly and I'm getting module not found errors.

Additionally, the `@theme-original` aliases that should be created for swizzled components are not being generated at all, making it impossible to import the original theme components when customizing them.

### Reproduction

1. Set up a Docusaurus project with a custom theme
2. Try to import a theme component using `@theme/ComponentName`
3. The import fails or resolves to the wrong file

For swizzled components:
1. Swizzle a theme component
2. Try to import the original component using `@theme-original/ComponentName`
3. The import fails because the alias was never created

### Expected behavior

- `@theme` aliases should resolve to the correct theme component files based on the relative source path
- `@theme-original` aliases should be created when `addOriginalAlias` is true, allowing swizzled components to import the original theme components

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
