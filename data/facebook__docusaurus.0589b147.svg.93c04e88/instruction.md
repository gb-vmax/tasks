# Bug Report

### Describe the bug

SVG imports are no longer working as React components in my TypeScript/JSX files. After updating, all SVG files are being treated as URLs instead of being processed by SVGR, which breaks my existing code that imports SVGs as components.

### Reproduction

```tsx
import Logo from './logo.svg';

function Header() {
  // This used to work - Logo was a React component
  // Now it's just a URL string
  return <Logo />;
}
```

The above code now throws an error because `Logo` is a string (URL) instead of a React component.

### Expected behavior

When importing SVG files from `.tsx`, `.jsx`, or `.mdx` files, they should be processed by SVGR and available as React components, not as URL strings. The SVGR loader should take precedence for React source files.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking all my existing SVG imports that rely on SVGR transformation. The URL loader seems to be taking priority over the SVGR loader now.

---
Repository: /testbed
