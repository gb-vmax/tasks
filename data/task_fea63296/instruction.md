You are a mobile build engineer maintaining build artifact directories for Android and iOS teams. In your home directory at <code>/home/user</code>, you currently have an outdated structure. Please perform the following steps to prepare the directories for upcoming releases. Be precise, as the results will be validated by an automated system.

1. **Reorganize Directories**: 
    - Create a main directory called <code>/home/user/build_artifacts</code>. 
    - Inside <code>build_artifacts</code>, create two subdirectories: <code>android</code> and <code>ios</code>.

2. **Move and Clean Files**:
    - If any files or subdirectories named <code>android_old</code> or <code>ios_old</code> exist anywhere under <code>/home/user</code> (at any depth), move their contents into the newly created <code>/home/user/build_artifacts/android</code> or <code>/home/user/build_artifacts/ios</code> accordingly. Once the contents are moved, delete the now-empty <code>android_old</code> or <code>ios_old</code> directories.
    - Do not overwrite existing files in the destination; if there are filename conflicts, preserve both by renaming the moved file with a <code>_legacy</code> suffix before the extension. (E.g., <code>app-release.apk</code> becomes <code>app-release_legacy.apk</code>.)

3. **Generate Directory Report**:
    - For verification, create a log file at <code>/home/user/build_artifacts/artifact_report.log</code>. 
    - In this log file, list the full path of every file (excluding directories) inside both <code>android</code> and <code>ios</code> subdirectories, one file per line, sorted alphabetically.
    - After the list, write two additional lines in the report in this format:
        - <code>Android files: N</code>
        - <code>iOS files: M</code>
      where <code>N</code> and <code>M</code> are the total number of files under <code>android</code> and <code>ios</code>, respectively.

4. **Permissions**:
    - Ensure that the <code>build_artifacts</code> directory and all files/subdirectories under it are owned by <code>user</code>, and are readable and writable by <code>user</code> only (permission 700 for directories, 600 for files).

Please ensure the report log matches the precise format described, as it will be checked automatically. The directory tree must be as described, and only required files and directories should remain. You may use as much terminal output as necessary to guide your steps.
