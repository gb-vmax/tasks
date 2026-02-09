# Bug Report

### Describe the bug

I'm encountering an issue with TOC (Table of Contents) slice imports in MDX files. When the loader tries to add a named import for a TOC slice, the imported and local identifiers are getting swapped, causing the wrong variable names to be used in the generated code.

### Reproduction

When processing an MDX file that requires a TOC slice import, the generated import statement has the names reversed:

```js
// What gets generated (incorrect):
import { tocSliceImportName as tocExportName } from '@theme/TOCSlice';

// What should be generated (correct):
import { tocExportName as tocSliceImportName } from '@theme/TOCSlice';
```

This causes runtime errors because the code is trying to reference a variable with the wrong name.

### Steps to reproduce:
1. Create an MDX file with headings that should generate a TOC
2. Process it through the mdx-loader
3. Check the generated import statement for the TOC slice
4. The imported/local names are reversed

### Expected behavior

The import statement should correctly map the exported name to the local name, not the other way around. The `imported` field should contain the actual export name from the module, and the `local` field should contain the name used locally in the file.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
