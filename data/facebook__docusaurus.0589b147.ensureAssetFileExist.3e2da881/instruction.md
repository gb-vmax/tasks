# Bug Report

### Describe the bug

I'm experiencing an issue where valid asset files (images, etc.) referenced in my MDX files are throwing "not found" errors during build, even though the files clearly exist in the correct location.

### Reproduction

1. Create an MDX file with a reference to an existing asset:
```md
![My Image](./assets/image.png)
```

2. Ensure the asset file actually exists at `./assets/image.png`
3. Run the build

### Expected behavior

The build should succeed since the asset file exists and is correctly referenced.

### Actual behavior

Getting an error like:
```
Asset <path-to-mdx-file> used in <path-to-asset> not found.
```

This is really confusing because:
- The file paths in the error message seem backwards (showing the MDX file as the asset and vice versa)
- The asset file definitely exists - I can see it in my file system
- This started happening recently, was working fine before

It seems like the asset validation logic is inverted somehow? Valid assets are being rejected while presumably missing assets would be accepted (though I haven't tested that).

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
