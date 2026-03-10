Hey, I need help with a backup step in my translation release workflow. I'm a localization engineer and I've just finished updating the translation files for our app's latest release. Before I ship them, I need to archive the translations directory and create a manifest so the release team knows exactly what's included.

The translation files live at `/home/user/translations`. This directory contains several locale subdirectories (like `en_US`, `fr_FR`, `de_DE`, etc.), each with one or more `.po` files inside.

Here's what I need you to do:

**Step 1: Create a compressed archive**

Create a gzip-compressed tar archive of the entire `/home/user/translations` directory. Save the archive to `/home/user/releases/translations_v2.tar.gz`. The archive should store the directory as `translations/` (i.e., use a relative path so that extracting it produces a `translations/` folder, not an absolute path). Make sure the `/home/user/releases/` directory exists before creating the archive.

**Step 2: Generate a manifest file**

List every file stored inside the archive (just the file paths, not directories) and write them to `/home/user/releases/translations_v2.manifest`. The manifest should meet these requirements:

- One file path per line
- Paths should be exactly as they appear inside the archive (e.g., `translations/fr_FR/app.po`)
- The list must be sorted alphabetically (ascending)
- No blank lines, no headers, no trailing whitespace

**Step 3: Append a checksum**

Compute the MD5 checksum of `/home/user/releases/translations_v2.tar.gz` and append a single line to the bottom of `/home/user/releases/translations_v2.manifest` in exactly this format:

```
MD5: <checksum>
```

Where `<checksum>` is the hex digest produced by `md5sum` (the 32-character hex string only, not the filename).

The final manifest file should look something like this (with your actual paths and checksum):

```
translations/de_DE/app.po
translations/en_US/app.po
translations/en_US/errors.po
translations/fr_FR/app.po
MD5: d41d8cd98f00b204e9800998ecf8427e
```

Please make sure the archive and manifest end up in `/home/user/releases/` and that the manifest is named exactly `translations_v2.manifest`.
