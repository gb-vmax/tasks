# Bug Report

### Describe the bug

After a recent update, API spec documents are being modified unexpectedly when loaded. Specifically, file names are being altered and content is being normalized even when not necessary.

### Reproduction

I have an API spec with the following properties:
```js
{
  fileName: "My  API  Spec",  // Note: multiple spaces between words
  contentType: "yaml",
  contents: "openapi: 3.0.0\r\ninfo:\r\n  title: Test"  // Windows line endings
}
```

After loading this spec, I noticed:
1. The fileName has been changed to "My API Spec" (spaces collapsed)
2. The contents line endings have been normalized from `\r\n` to `\n`

This is happening even for existing documents that were previously saved with these exact values. I didn't expect the system to automatically modify my file names or content without explicitly requesting it.

### Expected behavior

Documents should be loaded as-is without automatic modifications to file names or content. If normalization is needed, it should either:
- Only apply to newly created documents
- Be explicitly triggered by the user
- Preserve the original values for existing documents

### Additional context

This seems to be affecting all API spec documents in my workspace. I'm particularly concerned about the line ending changes as I need to maintain consistent formatting for version control purposes.

---
Repository: /testbed
