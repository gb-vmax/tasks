# Bug Report

### Describe the bug

SVG imports are not being processed by SVGR in React/MDX files anymore. When importing SVG files as React components, they are being treated as regular URL assets instead of being transformed into React components.

### Reproduction

```jsx
import Logo from './logo.svg';

function MyComponent() {
  // This now returns a URL string instead of a React component
  return <Logo />;
}
```

Expected: SVG should be imported as a React component that can be used directly in JSX.
Actual: SVG is imported as a URL string, causing a runtime error when trying to use it as a component.

### Steps to reproduce

1. Create a React/TypeScript component file (.tsx or .jsx)
2. Import an SVG file using `import Logo from './logo.svg'`
3. Try to use it as a JSX component: `<Logo />`
4. The component fails to render and throws an error

This affects SVG imports in:
- `.tsx` files
- `.jsx` files  
- `.mdx` files

### Expected behavior

SVG files imported in React source files should be transformed into React components via SVGR loader, allowing them to be used directly as JSX elements.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
