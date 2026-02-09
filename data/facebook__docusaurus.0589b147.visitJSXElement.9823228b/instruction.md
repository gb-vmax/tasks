# Bug Report

### Describe the bug

When using JSX components in MDX files that don't have a corresponding import declaration, the table of contents (TOC) generation is adding invalid slice imports. This causes the TOC to reference non-existent imports for components that aren't actually imported in the file.

### Reproduction

Create an MDX file with a JSX element that doesn't have an import:

```mdx
# My Document

Some content here.

<SomeComponent />

## Section 1

More content.
```

The TOC generation will try to create a slice import for `SomeComponent` even though there's no import declaration for it in the file. This results in the TOC trying to reference an import that doesn't exist.

### Expected behavior

The TOC should only add slice imports for components that actually have valid import declarations. If a JSX element is used without a corresponding import, it shouldn't add a TOC slice entry for it.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
