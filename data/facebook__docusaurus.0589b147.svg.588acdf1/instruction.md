# Bug Report

### Describe the bug

SVG imports in React/JSX files are not being processed by SVGR anymore. Instead of getting a React component, I'm getting a URL string when importing SVG files with the default import syntax.

### Reproduction

```jsx
import Logo from './logo.svg';

function Header() {
  // Logo is now a string URL instead of a React component
  return <Logo />; // This throws an error
}
```

Expected: `Logo` should be a React component that I can use directly in JSX
Actual: `Logo` is a URL string

This is breaking all my SVG imports in `.tsx`, `.jsx`, and `.mdx` files. The SVGs are being treated as regular assets instead of being transformed into React components.

### Expected behavior

SVG files imported in React/TypeScript files should be transformed into React components via SVGR, not loaded as URL strings.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
