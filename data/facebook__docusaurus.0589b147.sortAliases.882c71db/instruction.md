# Bug Report

### Describe the bug

I'm experiencing an issue with theme component alias resolution in Docusaurus. When I have custom theme components with similar paths, the wrong component is being loaded. Specifically, when I create a custom `@theme/NavbarItem` component and also have a `@theme/NavbarItem/LocaleDropdown` component, the navbar item doesn't use my custom implementation.

### Reproduction

1. Create a custom theme component at `src/theme/NavbarItem/index.tsx`
2. Also have a component at `src/theme/NavbarItem/LocaleDropdown/index.tsx`
3. Build the site
4. The custom `NavbarItem` component is not being used, even though it should take precedence

The alias resolution seems to be ordering these paths incorrectly, causing the more specific path to override the general one when it shouldn't.

### Expected behavior

When I swizzle or create a custom `@theme/NavbarItem` component, it should be used by the application. The presence of nested components like `@theme/NavbarItem/LocaleDropdown` shouldn't affect the resolution of the parent component alias.

The aliases should be sorted so that:
- `@theme/NavbarItem/LocaleDropdown` comes before `@theme/NavbarItem`
- This ensures webpack resolves the more specific paths first

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This might be related to how webpack resolves aliases when there are nested component paths.

---
Repository: /testbed
