"""
Custom FileSystemStorage 
Django FileSystemStorage gives error when using fs.save method (OSError : Function not implemented ) becaus of fcntl.lock ,
for this reason I have to Overwite save method and remove the error creating code
"""

from django.core.files.storage import FileSystemStorage
import os
class CustomFileSystemStorage(FileSystemStorage):
  def _save(self, name, content):
        full_path = self.path(name)
        # Create any intermediate directories that do not exist.
        directory = os.path.dirname(full_path)
        try:
            if self.directory_permissions_mode is not None:
                # Set the umask because os.makedirs() doesn't apply the "mode"
                # argument to intermediate-level directories.
                old_umask = os.umask(0o777 & ~self.directory_permissions_mode)
                try:
                    os.makedirs(
                        directory, self.directory_permissions_mode, exist_ok=True
                    )
                finally:
                    os.umask(old_umask)
            else:
                os.makedirs(directory, exist_ok=True)
        except FileExistsError:
            raise FileExistsError("%s exists and is not a directory." % directory)

        # There's a potential race condition between get_available_name and
        # saving the file; it's possible that two threads might return the
        # same name, at which point all sorts of fun happens. So we need to
        # try to create the file, but if it already exists we have to go back
        # to get_available_name() and try again.

        while True:
            try:
                # This file has a file path that we can move.
                if hasattr(content, "temporary_file_path"):
                    file_move_safe(content.temporary_file_path(), full_path)

                # This is a normal uploadedfile that we can stream.
                else:
                    # The current umask value is masked out by os.open!
                    fd = os.open(full_path, self.OS_OPEN_FLAGS, 0o666)
                    _file = None
                    try:
                        for chunk in content.chunks():
                            if _file is None:
                                mode = "wb" if isinstance(chunk, bytes) else "wt"
                                _file = os.fdopen(fd, mode)
                            _file.write(chunk)
                    finally:
                        if _file is not None:
                            _file.close()
                        else:
                            os.close(fd)
            except FileExistsError:
                # A new name is needed if the file exists.
                name = self.get_available_name(name)
                full_path = self.path(name)
            else:
                # OK, the file save worked. Break out of the loop.
                break

        if self.file_permissions_mode is not None:
            os.chmod(full_path, self.file_permissions_mode)

        # Ensure the saved path is always relative to the storage root.
        name = os.path.relpath(full_path, self.location)
        # Ensure the moved file has the same gid as the storage root.
        self._ensure_location_group_id(full_path)
        # Store filenames with forward slashes, even on Windows.
        return str(name).replace("\\", "/")

print("file system runner")
#fs = CustomFileSystemStorage()
#fs.save("cc00.jpg",ContentFile(open("Screenshot_20230819-204150.jpg","rb")))