from rest_framework import permissions

class IsAdminOrEditOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin to create and delete of an object
    and others to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in ['GET' , 'PUT']:
            if request.method == 'PUT' and 'filename' in request.data:
                    if request.data['filename'] != obj.filename:
                        self.message = 'Filename of the job cannot be edited!'
                        return False    
            return True
        # Write permissions are only allowed to the admin.
        elif (request.method == 'POST') and (request.user.is_staff):
            return True
        return False


class IsAdminUser(permissions.IsAdminUser):
    pass