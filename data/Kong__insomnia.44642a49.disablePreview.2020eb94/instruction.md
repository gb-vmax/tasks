# Bug Report

### Describe the bug

The `disablePreview` functionality for the Prompt template tag isn't working as expected. When using the "Default to Last Value" option with the value set to `false`, the preview should be disabled but it's not happening.

### Reproduction

```js
// Create a prompt template tag with the following args:
const args = [
  { value: 'Title' },           // Title
  { value: 'Label' },           // Label  
  { value: 'Default Value' },   // Default Value
  { value: 'Storage Key' },     // Storage Key
  { value: false },             // Mask Text (disabled)
  { value: false }              // Default to Last Value (disabled)
]

// The preview should be disabled when "Default to Last Value" is false,
// but currently it only disables when "Mask Text" is true
```

### Expected behavior

The preview should be disabled in two cases:
1. When "Mask Text" is enabled (set to `true`)
2. When "Default to Last Value" is disabled (set to `false`)

Currently, only the first case works. The second case is being ignored, so users can still see previews even when they've explicitly disabled the "Default to Last Value" option.

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
