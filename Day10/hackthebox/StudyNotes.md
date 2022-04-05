Recursively download files from smb share using smbclient:
  1. smbclient '\\server\share'
  2. mask ""
  3. recurse ON
  4. prompt OFF

OR 
```
smbclient '\\server\share' -N -c 'prompt OFF;recurse ON;cd 'path\to\directory\';lcd '~/path/to/download/to/';mget *'`
```
