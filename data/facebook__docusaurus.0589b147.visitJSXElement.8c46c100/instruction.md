# Bug Report

### Describe the bug

When using JSX components (like `<Partial/>`) in MDX files, the table of contents (TOC) is not being generated correctly. It appears that JSX elements are being skipped during TOC collection, causing the TOC to be incomplete or missing entries that should be included from imported components.

### Reproduction

```mdx
import Partial from './partial.mdx';

# Main Heading

Some content here.

<Partial />

## Another Heading
```

When the above MDX file is processed, the TOC items from the `<Partial/>` component are not included in the generated table of contents, even though the component is properly imported and should contribute its headings to the TOC.

### Expected behavior

JSX elements that are imported components should have their TOC slices properly collected and included in the parent document's table of contents. The component name should be recognized, the import declaration should be found, and the appropriate TOC slice import should be added.

### System Info
- Docusaurus version: Latest
- MDX loader: docusaurus-mdx-loader

---
Repository: /testbed
