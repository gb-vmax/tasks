# Bug Report

### Describe the bug

When using template tags with OAuth2 attributes, the visibility logic isn't working as expected. Attributes that should be hidden based on context information are still being displayed in the UI.

### Reproduction

```js
// Template tag with OAuth2 attribute
const args = [
  { value: 'oauth2-token' },
  { value: 'someValue' },
  { value: { hasOAuth2: false } }
];

// The hide function should return true when OAuth2 is not available
// but the attribute is still visible in the template editor
```

### Steps to reproduce:
1. Create a template tag with an oauth2-related attribute
2. Pass context info indicating OAuth2 is not available (hasOAuth2: false)
3. The attribute field is still shown in the UI when it should be hidden

### Expected behavior

OAuth2-related attributes should be automatically hidden when the context indicates OAuth2 is not available in the current environment. The hide function should check for the `hasOAuth2` flag in the context info and hide oauth2 attributes accordingly.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
