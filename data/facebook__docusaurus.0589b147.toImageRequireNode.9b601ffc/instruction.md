# Bug Report

### Bug: Image references with URL fragments are broken

I'm experiencing an issue where markdown images that include URL fragments (hash anchors) are not working correctly. The images fail to load and the fragment part seems to be getting lost or mishandled.

### Reproduction

In my MDX file, I have an image reference like this:

```markdown
![My Image](./assets/image.png#thumbnail)
```

After the page loads, the image doesn't display correctly. It seems like the hash fragment `#thumbnail` is not being processed properly in the image path.

### Expected behavior

The image should load correctly with the hash fragment preserved in the URL. This is useful for cases where you want to apply specific styling or behavior based on the fragment identifier.

### Additional context

This affects any image reference that uses a hash fragment in the URL. Regular images without fragments work fine, but as soon as you add something like `#thumbnail` or `#icon`, the image path gets corrupted.

---
Repository: /testbed
