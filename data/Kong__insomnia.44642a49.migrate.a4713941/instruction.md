# Bug Report

### Describe the bug

After a recent update, API spec files are having their filenames automatically modified. When loading an existing spec, the filename gets changed even though I didn't rename it. For example, a file named `my-api` gets changed to `my-api.yaml` or `my-api.json`.

### Reproduction

1. Create an API spec with a filename that doesn't have an extension (e.g., `openapi-spec`)
2. Save the spec
3. Reload or reopen the spec
4. The filename is now modified to include an extension (e.g., `openapi-spec.yaml`)

This also happens when the extension doesn't match the content type:
1. Create a spec with filename `api.json` but with YAML content
2. Save and reload
3. Filename gets changed to `api.yaml`

### Expected behavior

The filename should remain unchanged unless I explicitly rename it. If I name my file `my-api` without an extension, it should stay as `my-api`. The system shouldn't be automatically appending extensions or modifying my filenames.

### Additional context

This is causing issues with our workflow where we have specific naming conventions that don't always include file extensions. The automatic renaming is breaking our file tracking and version control.

---
Repository: /testbed
