# Bug Report

### Describe the bug

After a recent update, I'm seeing duplicate headers being generated when importing OpenAPI 3 specifications. The importer seems to be creating multiple header entries with the same name (case-insensitive), which causes issues when making requests.

### Reproduction

When importing an OpenAPI 3.0 spec with parameter headers defined at different levels (e.g., path-level and operation-level), or when headers are specified with different casing (like "Accept" and "accept"), the importer doesn't deduplicate them properly.

For example, if you have:
- A path-level header parameter for "content-type"
- An operation-level header parameter for "Content-Type"

Both headers end up in the final request, even though they should be treated as the same header (HTTP headers are case-insensitive).

### Expected behavior

The importer should deduplicate headers by treating header names as case-insensitive. When duplicate headers are found:
- If one is disabled and the other is enabled, keep the enabled one
- If both have the same enabled/disabled state, keep the first occurrence

### System Info
- Insomnia version: latest
- OS: macOS

This is causing problems with APIs that are strict about duplicate headers or when the duplicate headers have conflicting values.

---
Repository: /testbed
