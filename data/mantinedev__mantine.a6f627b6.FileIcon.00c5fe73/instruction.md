# Bug Report

### Describe the bug

The `FileIcon` component in `CodeHighlightTabs` is not rendering the file icon when `getFileIcon` is provided but `fileName` is undefined or null. The current logic requires both `getFileIcon` AND `fileName` to be truthy, but there are valid use cases where you might want to call `getFileIcon` without a `fileName` parameter.

### Reproduction

```tsx
import { CodeHighlightTabs } from '@mantine/code-highlight';

const customGetFileIcon = (fileName) => {
  // Custom icon logic that can handle undefined fileName
  return <MyCustomIcon />;
};

// This doesn't render the icon even though getFileIcon is provided
<CodeHighlightTabs
  code={[
    {
      fileName: undefined, // or null
      code: 'console.log("test")',
      language: 'tsx',
    },
  ]}
  getFileIcon={customGetFileIcon}
/>
```

### Expected behavior

When `getFileIcon` is provided, it should be called regardless of whether `fileName` is present. The `getFileIcon` function should be responsible for handling cases where `fileName` might be undefined/null, not the component itself.

The icon should render as long as `getFileIcon` is provided, even if `fileName` is falsy.

### System Info

- @mantine/code-highlight version: latest
- React version: 18.x

---
Repository: /testbed
