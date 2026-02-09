# Bug Report

### Describe the bug

After a recent update, the `DateInput` component is throwing TypeScript errors when trying to use it without providing a `dateParser` prop. It appears that `dateParser` has been changed from an optional prop to a required one, which breaks existing code that was relying on the default behavior.

### Reproduction

```tsx
import { DateInput } from '@mantine/dates';

// This now throws a TypeScript error:
// Property 'dateParser' is missing in type '{}' but required in type 'DateInputProps'
<DateInput />

// Also fails with other props but no dateParser:
<DateInput
  value={new Date()}
  onChange={(date) => console.log(date)}
/>
```

### Expected behavior

The `dateParser` prop should be optional, allowing the component to work with its default date parsing behavior when not explicitly provided. This was working fine in previous versions.

### System Info
- @mantine/dates version: latest
- TypeScript version: 5.x

---
Repository: /testbed
