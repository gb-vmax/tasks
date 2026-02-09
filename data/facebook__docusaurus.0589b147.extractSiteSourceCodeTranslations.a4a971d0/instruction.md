# Bug Report

### Describe the bug

When extracting translations from source code files, duplicate translation keys are being generated. It appears that source code files are being processed twice, resulting in duplicate entries in the translation extraction output.

### Reproduction

1. Set up a Docusaurus site with translation files
2. Add a translation key in a source code file using `<Translate>` or the `translate()` function
3. Run the translation extraction process
4. Check the extracted translations - each key appears twice

Example:
```jsx
// In a component file
<Translate id="homepage.title">Welcome</Translate>
```

After extraction, the translation key `homepage.title` appears duplicated in the output.

### Expected behavior

Each translation key should only appear once in the extracted translations, even if the same key is used in multiple places. The extraction process should deduplicate entries or only process each source file once.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
