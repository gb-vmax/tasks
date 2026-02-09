# Bug Report

### Describe the bug

The edit URL generation for localized documentation files is not working as expected. When using localized docs with `editLocalizedFiles` option, the wrong edit URL is being generated.

### Reproduction

1. Set up a docs plugin with localization enabled
2. Configure `editUrl` as a string with `editLocalizedFiles: true`
3. Create a localized version of a documentation file
4. Check the generated edit URL for the localized file

The edit URL points to the wrong location - it seems like the logic for determining whether to use `editUrl` or `editUrlLocalized` is inverted.

### Expected behavior

When `editLocalizedFiles` is set to `true` and the file is localized, the edit URL should use `editUrlLocalized`. When the file is not localized or `editLocalizedFiles` is `false`, it should use the base `editUrl`.

Currently it appears to be doing the opposite - using `editUrlLocalized` when the file is NOT localized, and using `editUrl` when it IS localized.

### Additional context

This affects the "Edit this page" links in the documentation, causing them to point to incorrect paths in the repository when working with localized content.

---
Repository: /testbed
