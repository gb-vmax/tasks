# Bug Report

### Describe the bug

The `Interpolate` component is not rendering text correctly. When I try to use it with template strings and values, the interpolated content doesn't appear in the output.

### Reproduction

```jsx
import Interpolate from '@docusaurus/Interpolate';

// This renders nothing instead of the expected text
<Interpolate
  values={{
    name: <strong>John</strong>,
    count: 5
  }}
>
  {'Hello {name}, you have {count} messages'}
</Interpolate>
```

Expected output: "Hello **John**, you have 5 messages"
Actual output: Empty string or missing content

### Steps to reproduce
1. Create a component using `Interpolate`
2. Pass a string with placeholders like `{name}`
3. Provide values object with corresponding keys
4. The component renders blank or shows unexpected output

The static text parts and the interpolated values both seem to disappear. This worked fine in previous versions.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
