# Bug Report

### Describe the bug

When exporting documents without PDF conversion enabled, the export process is using the wrong format parameter. The system appears to be using `pdfFormat` instead of the regular `format` field, which causes exports to fail or produce unexpected results when PDF conversion is not requested.

### Reproduction

```js
// Export a document with PDF conversion disabled
const selectedFormat = {
  format: 'json',
  convertToPdf: false,
  pdfFormat: undefined
};

// Call the export function
await exportDocument(selectedFormat);

// Expected: Document exports as JSON
// Actual: Export fails or uses undefined format
```

### Steps to reproduce:
1. Select a document to export
2. Choose a non-PDF format (e.g., JSON, YAML)
3. Ensure "Convert to PDF" option is disabled
4. Attempt to export
5. The export uses the wrong format parameter

### Expected behavior

When `convertToPdf` is false, the export should use the `format` field from the selected format options, not the `pdfFormat` field. The document should export successfully in the requested format.

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
