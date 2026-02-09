# Bug Report

### Describe the bug

I'm experiencing an issue with the `mod` prop on Box components. When passing mod attributes, they're not being properly formatted as data attributes in the rendered HTML.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// This should render with data-active="true" attribute
<Box mod={{ active: true }}>
  Content
</Box>

// Expected output: <div data-active="true">Content</div>
// Actual output: <div dataactive="true">Content</div>
```

The data attributes are missing the hyphen separator, resulting in malformed attribute names like `dataactive` instead of `data-active`.

### Expected behavior

The mod prop should generate properly formatted data attributes with the `data-` prefix and hyphen separator. For example:
- `mod={{ active: true }}` should produce `data-active="true"`
- `mod={{ custom: 'value' }}` should produce `data-custom="value"`

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
