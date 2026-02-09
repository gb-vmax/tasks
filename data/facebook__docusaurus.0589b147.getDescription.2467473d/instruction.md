# Bug Report

### Describe the bug

When trying to swizzle theme components, the component descriptions are not being displayed correctly. Instead of showing the specific description for each component, all components seem to show the same fallback description or incorrect descriptions.

### Reproduction

```bash
# Try to swizzle any theme component
npx docusaurus swizzle @docusaurus/theme-classic <ComponentName>
```

When listing available components or viewing component information during the swizzle process, the descriptions don't match the actual components - they all appear to be the same or don't correspond to the right component.

### Expected behavior

Each theme component should display its own unique description (if available) when using the swizzle command. The description should help users understand what each component does before deciding to swizzle it.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
