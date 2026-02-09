# Bug Report

### Describe the bug

When using JSX components in MDX files that are not imported (e.g., built-in components or components from other sources), the TOC generation fails because it tries to add TOC slice imports for components that don't have an import declaration.

### Reproduction

Create an MDX file with a JSX element that doesn't have a corresponding import statement:

```mdx
# My Document

<SomeComponent />

## Section 1
Content here
```

When the component `SomeComponent` is not explicitly imported in the MDX file (for example, if it's a global component or provided through MDX context), the TOC processing will attempt to create a TOC slice for it even though there's no import declaration to work with.

### Expected behavior

The TOC generation should only create TOC slices for components that actually have import declarations. Components without imports should be skipped or handled gracefully without breaking the build.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
