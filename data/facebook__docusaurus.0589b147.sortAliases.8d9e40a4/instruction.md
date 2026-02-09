# Bug Report

### Describe the bug

I'm experiencing an issue with theme component aliasing in Docusaurus where more specific theme aliases are being overridden by less specific ones. When I try to create a custom component that extends another theme component (e.g., a custom `NavbarItem/LocaleDropdown` alongside a custom `NavbarItem`), the wrong component gets resolved.

### Reproduction

1. Create a custom theme component at `@theme/NavbarItem`
2. Create another custom theme component at `@theme/NavbarItem/LocaleDropdown`
3. Try to use the `LocaleDropdown` component

Expected: The more specific `@theme/NavbarItem/LocaleDropdown` should be used
Actual: The less specific `@theme/NavbarItem` is being resolved instead

### Steps to reproduce

```
src/theme/
├── NavbarItem/
│   ├── index.js
│   └── LocaleDropdown.js
```

When the site builds, imports to `@theme/NavbarItem/LocaleDropdown` incorrectly resolve to `@theme/NavbarItem` instead of the more specific path.

### Expected behavior

More specific theme aliases (with longer paths) should take precedence over less specific ones. If I have both `@theme/NavbarItem` and `@theme/NavbarItem/LocaleDropdown` defined, an import to `@theme/NavbarItem/LocaleDropdown` should resolve to the more specific alias, not the parent one.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
