# Bug Report

### Describe the bug

The `FileIcon` component is not rendering correctly when only a `fileIcon` prop is provided without a `fileName`. The icon should be displayed regardless of whether `fileName` is present or not, but currently it's being skipped.

### Reproduction

```tsx
import { FileIcon } from '@mantine/code-highlight';

// This doesn't render anything even though fileIcon is provided
<FileIcon 
  fileIcon={<MyCustomIcon />}
  className="icon-class"
  style={{ color: 'blue' }}
/>
```

### Expected behavior

When `fileIcon` prop is provided, it should be rendered even if `fileName` is not specified. The `fileName` prop should only be required when using the `getFileIcon` function to dynamically generate icons based on file names.

### System Info

- @mantine/code-highlight version: latest
- React version: 18.x

---
Repository: /testbed
