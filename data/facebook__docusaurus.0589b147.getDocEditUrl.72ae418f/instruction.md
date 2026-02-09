# Bug Report

### Describe the bug

The edit URL generation for localized documentation is broken. When using a custom `editUrl` function or the `editLocalizedFiles` option, the generated edit URLs point to the wrong paths - they seem to be swapped between localized and non-localized content.

### Reproduction

Setup:
1. Configure a docs plugin with `editLocalizedFiles: true`
2. Create both localized and non-localized versions of a document
3. Check the generated edit URLs for each version

For localized docs, the edit URL points to the non-localized path, and vice versa.

Example config:
```js
{
  editUrl: 'https://github.com/user/repo/edit/main/',
  editLocalizedFiles: true,
}
```

When viewing a localized document (e.g., in `/i18n/fr/docusaurus-plugin-content-docs/current/`), the edit link incorrectly points to the non-localized version's path instead of the localized one.

The same issue occurs when using a custom `editUrl` function - the `versionDocsDirPath` parameter contains the wrong path.

### Expected behavior

- For localized docs with `editLocalizedFiles: true`, the edit URL should point to the localized file path
- For non-localized docs, the edit URL should point to the non-localized file path
- The `versionDocsDirPath` in custom `editUrl` functions should correctly reflect whether the document is localized or not

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
