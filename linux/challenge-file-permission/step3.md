# Set The File Permissions

`chmod` is command that used to change the access rights of a file or directory on Linux OS, and use it to control the access rights of files or directories.

Now you need to use the `chmod` command to set the file permissions.

> Tip: You need to use an administrator account or use an account with sudo privileges

## Result Example

```bash
-rwxr-x--- 1 user1 group1 0 Feb 16 18:50 target_file
```

## Requirements

- must use `chmod` command.
- the file must be readable, writable, and executable by the owner.
- the file must be readable and writable by the group.
- the file must not be readable, writable, or executable by anyone else.
