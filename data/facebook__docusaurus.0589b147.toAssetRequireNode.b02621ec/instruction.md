# Bug Report

### Describe the bug

Links to assets with URL fragments (hash anchors) are not working correctly. When linking to files like PDFs with a hash fragment (e.g., `file.pdf#page=2`), the hash portion is being lost or duplicated in the generated output.

### Reproduction

Create a markdown file with a link to an asset that includes a hash fragment:

```md
[View PDF page 2](./assets/document.pdf#page=2)
```

The hash fragment `#page=2` is not being handled correctly in the generated link. The expected behavior would be to preserve the hash fragment so that the PDF opens to the specified page.

### Expected behavior

The link should preserve the hash fragment and generate proper output that includes `#page=2` in the final href attribute, allowing the PDF to open at the correct page.

### System Info
- Docusaurus version: latest
- MDX loader version: latest

---
Repository: /testbed
