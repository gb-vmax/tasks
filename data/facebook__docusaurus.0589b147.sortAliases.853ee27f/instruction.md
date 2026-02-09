# Bug Report

### Describe the bug

When using theme aliases with nested paths, the webpack alias resolution is not working correctly. More specific aliases (like `@theme/NavbarItem/LocaleDropdown`) are being resolved before their parent aliases (like `@theme/NavbarItem`), causing the wrong components to be loaded.

### Reproduction

```js
// Given these theme aliases:
{
  '@theme/NavbarItem': '/path/to/NavbarItem',
  '@theme/NavbarItem/LocaleDropdown': '/path/to/NavbarItem/LocaleDropdown',
  '@theme/Footer': '/path/to/Footer'
}

// When importing @theme/NavbarItem/LocaleDropdown
import LocaleDropdown from '@theme/NavbarItem/LocaleDropdown';

// The alias resolution picks up @theme/NavbarItem first
// resulting in an incorrect path like:
// /path/to/NavbarItem/LocaleDropdown instead of /path/to/NavbarItem/LocaleDropdown
```

### Expected behavior

More specific aliases (those with deeper paths) should be matched first before their parent aliases. So `@theme/NavbarItem/LocaleDropdown` should resolve before `@theme/NavbarItem`.

The alias sorting should ensure that:
- Child paths are prioritized over parent paths
- `@theme/NavbarItem/LocaleDropdown` comes before `@theme/NavbarItem`
- `@theme/Navbar/Items/Default` comes before `@theme/Navbar/Items` which comes before `@theme/Navbar`

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
