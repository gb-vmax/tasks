# Bug Report

### Describe the bug

CSS variables are not being applied correctly when using `MantineProvider`. The generated CSS variable string appears to be malformed, causing styles to not be injected properly into the DOM.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider
      theme={{
        cssVariablesResolver: () => ({
          variables: {
            '--mantine-color-primary': '#228be6',
            '--mantine-spacing-md': '16px',
            '--mantine-font-size-lg': '18px',
          },
          light: {},
          dark: {},
        }),
      }}
    >
      <div>Content</div>
    </MantineProvider>
  );
}
```

When inspecting the generated CSS, the variables are not formatted correctly. Expected format would be something like:

```css
--mantine-color-primary: #228be6; --mantine-spacing-md: 16px; --mantine-font-size-lg: 18px;
```

But the actual output is incorrect and the styles don't apply.

### Expected behavior

CSS variables should be properly formatted and injected into the style tag, allowing theme customization to work as expected. All defined CSS variables should be accessible and properly parsed by the browser.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
