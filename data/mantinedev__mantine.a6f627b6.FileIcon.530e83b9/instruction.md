# Bug Report

### Describe the bug

When using `CodeHighlightTabs` with a custom `fileIcon` prop, the icon doesn't render in the UI. The tab appears but the file icon is missing even though the prop is being passed correctly.

### Reproduction

```tsx
import { CodeHighlightTabs } from '@mantine/code-highlight';

const MyComponent = () => {
  return (
    <CodeHighlightTabs
      code={[
        {
          fileName: 'example.tsx',
          code: 'console.log("test")',
          language: 'tsx',
          fileIcon: <IconFile size={16} />
        }
      ]}
    />
  );
};
```

### Expected behavior

The custom file icon should be displayed in the tab. Instead, nothing appears where the icon should be.

### Additional context

This seems to have broken recently. The `fileIcon` prop is accepted but the icon component doesn't show up in the rendered output. If I don't provide a `fileIcon` and rely on `getFileIcon` instead, that works fine.

---
Repository: /testbed
