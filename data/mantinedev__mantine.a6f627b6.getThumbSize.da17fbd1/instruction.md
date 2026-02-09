# Bug Report

### Describe the bug

The ScrollArea component is completely broken - scrollbars are not rendering at all. When I try to use ScrollArea in my application, the content just overflows without any scrollbar appearing.

### Reproduction

```jsx
import { ScrollArea } from '@mantine/core';

function App() {
  return (
    <ScrollArea h={200}>
      <div style={{ height: 500 }}>
        Long content that should be scrollable
      </div>
    </ScrollArea>
  );
}
```

### Expected behavior

The ScrollArea should display a scrollbar when the content exceeds the container height. The scrollbar thumb should be visible and functional.

### Actual behavior

No scrollbar appears. The content just overflows the container. Looking at the browser console, I'm seeing errors related to `getThumbSize` not being defined or not being a function.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

This seems to have broken recently. The ScrollArea was working fine in my project before, but after updating it just stopped rendering scrollbars entirely.

---
Repository: /testbed
