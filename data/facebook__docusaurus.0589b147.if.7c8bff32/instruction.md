# Bug Report

### Describe the bug

When using the docs plugin with `editUrl` configured, the `editUrlLocalized` property is being set to an empty string `''` instead of `undefined` in certain cases. This causes issues with edit URL handling for localized documentation.

### Reproduction

```js
const options = {
  editUrl: 'https://github.com/myorg/myrepo/edit/main/',
  editCurrentVersion: false,
  path: '/docs'
}

// When getVersionEditUrls is called with these options
// editUrlLocalized is returned as '' instead of undefined
```

The issue occurs when `editUrl` is provided as a string (not a function). The logic seems to be checking the condition incorrectly, resulting in unexpected behavior for the localized edit URL.

### Expected behavior

When `editUrl` is provided as a string, both `editUrl` and `editUrlLocalized` should be properly computed or set to `undefined` if they cannot be determined. The `editUrlLocalized` should not be an empty string when it should be `undefined`.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
