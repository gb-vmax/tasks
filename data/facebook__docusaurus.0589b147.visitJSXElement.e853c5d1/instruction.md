# Bug Report

### Describe the bug

When using imported JSX components in MDX files, the table of contents (TOC) is not being generated correctly. Components that should be included in the TOC are being skipped, resulting in an incomplete or empty TOC.

### Reproduction

Create an MDX file with an imported component:

```mdx
import MyComponent from './MyComponent';

# Main Heading

Some content here.

<MyComponent />

## Subheading

More content.
```

The TOC should include the headings from `MyComponent`, but they are missing from the generated table of contents.

### Expected behavior

When a JSX component is imported and used in an MDX file, its headings should be extracted and included in the TOC. The TOC generation should process imported components and create the appropriate TOC slices.

### System Info

- Docusaurus version: latest
- MDX loader: @docusaurus/mdx-loader

This seems to have started happening recently. The TOC was working fine before with imported components.

---
Repository: /testbed
