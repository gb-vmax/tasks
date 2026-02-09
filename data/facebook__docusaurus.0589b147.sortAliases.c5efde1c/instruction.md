# Bug Report

### Describe the bug

The webpack alias resolution is not working correctly for theme components with nested paths. When I have both a parent component and a child component (e.g., `@theme/NavbarItem` and `@theme/NavbarItem/LocaleDropdown`), the wrong component gets resolved during the build.

### Reproduction

Here's what I'm experiencing:

1. Create a theme with nested components:
   - `@theme/NavbarItem`
   - `@theme/NavbarItem/LocaleDropdown`

2. Try to import `@theme/NavbarItem/LocaleDropdown` in your code

3. The import resolves to the wrong component or the build fails to find the correct component

### Expected behavior

The more specific/nested alias should take precedence. When importing `@theme/NavbarItem/LocaleDropdown`, it should resolve to the LocaleDropdown component, not the parent NavbarItem component.

The alias resolution order should prioritize longer, more specific paths over shorter parent paths.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken recently - the alias sorting logic might not be handling nested component paths correctly anymore.

---
Repository: /testbed
