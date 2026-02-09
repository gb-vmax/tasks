# Bug Report

### Describe the bug

The AppShell navbar is not displaying correctly at different breakpoints. When setting navbar width with responsive values, the navbar appears to be hidden or positioned incorrectly at the base breakpoint, and the collapse behavior seems inverted.

### Reproduction

```jsx
<AppShell
  navbar={{
    width: { base: 200, sm: 250, lg: 300 },
    breakpoint: 'sm',
    collapsed: { mobile: isCollapsed }
  }}
>
  <AppShell.Navbar>
    {/* Navbar content */}
  </AppShell.Navbar>
  <AppShell.Main>
    {/* Main content */}
  </AppShell.Main>
</AppShell>
```

### Expected behavior

- The navbar should be visible at the base breakpoint with the specified width (200px)
- The navbar should properly collapse/expand at the specified breakpoint
- When collapsed, the navbar should hide and the main content should expand to fill the space
- In fixed mode, the offset should be applied correctly when the navbar is visible

### Actual behavior

- The navbar width is not being applied at the base breakpoint
- The collapse behavior appears reversed - the navbar shows when it should be hidden and vice versa
- The main content offset is incorrect when the navbar is supposed to be collapsed

This seems to have started affecting both fixed and static layout modes. The navbar either doesn't show up at all or shows when it shouldn't.

---
Repository: /testbed
