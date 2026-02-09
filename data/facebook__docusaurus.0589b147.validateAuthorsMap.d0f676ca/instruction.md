# Bug Report

### Describe the bug

I'm experiencing an issue with the blog plugin's author validation. When I provide an invalid authors map in my blog configuration, the system doesn't properly reject it and continues processing with the invalid data. This leads to unexpected behavior downstream instead of getting a clear validation error upfront.

### Reproduction

```js
// In blog plugin configuration
const authorsMap = {
  john: {
    name: 'John Doe',
    // Missing required fields or invalid structure
    invalidField: 123
  }
}
```

When the authors map contains invalid data (wrong types, missing required fields, etc.), the validation seems to pass through instead of throwing an error. The error only shows up in console logs but doesn't actually prevent the build from continuing with bad data.

### Expected behavior

The plugin should throw a validation error and halt execution when the authors map doesn't match the expected schema. This would help catch configuration issues early rather than having them cause problems later in the build process.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-blog

---
Repository: /testbed
