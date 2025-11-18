# Permissions and Groups Setup Documentation

## Overview

This Django application implements a robust permissions and groups system to control access to documents. The system uses custom permissions defined in the `Document` model and enforces them through permission-protected views.

## Custom Permissions

### Document Model Permissions

The `Document` model in `accounts/models.py` defines four custom permissions:

- **can_view**: Permission to view documents
- **can_create**: Permission to create new documents
- **can_edit**: Permission to edit existing documents
- **can_delete**: Permission to delete documents

These permissions are defined in the model's Meta class:

```python
class Meta:
    permissions = [
        ('can_view', 'Can view document'),
        ('can_create', 'Can create document'),
        ('can_edit', 'Can edit document'),
        ('can_delete', 'Can delete document'),
    ]
```

## User Groups and Permission Assignment

### Recommended Groups Setup

#### 1. Viewers Group

**Permissions:**

- `accounts.can_view`

**Purpose:** Users in this group can only view documents but cannot create, edit, or delete them.

#### 2. Editors Group

**Permissions:**

- `accounts.can_view`
- `accounts.can_create`
- `accounts.can_edit`

**Purpose:** Users in this group can view, create, and edit documents but cannot delete them.

#### 3. Admins Group

**Permissions:**

- `accounts.can_view`
- `accounts.can_create`
- `accounts.can_edit`
- `accounts.can_delete`

**Purpose:** Users in this group have full access to all document operations.

## Setting Up Groups in Django Admin

### Step 1: Access Django Admin

1. Run the development server: `python manage.py runserver`
2. Navigate to `http://localhost:8000/admin/`
3. Log in with superuser credentials

### Step 2: Create Groups

1. Click on "Groups" under the "Authentication and Authorization" section
2. Click "Add Group"
3. Create the following groups:
   - **Viewers**
   - **Editors**
   - **Admins**

### Step 3: Assign Permissions to Groups

#### For Viewers Group:

1. Select "Viewers" group
2. In "Available permissions", find and add:
   - `accounts | document | Can view document`
3. Click "Save"

#### For Editors Group:

1. Select "Editors" group
2. In "Available permissions", find and add:
   - `accounts | document | Can view document`
   - `accounts | document | Can create document`
   - `accounts | document | Can edit document`
3. Click "Save"

#### For Admins Group:

1. Select "Admins" group
2. In "Available permissions", find and add:
   - `accounts | document | Can view document`
   - `accounts | document | Can create document`
   - `accounts | document | Can edit document`
   - `accounts | document | Can delete document`
3. Click "Save"

## Assigning Users to Groups

### Via Django Admin:

1. Go to "Users" section
2. Select a user
3. Scroll to "Groups" section
4. Select appropriate group(s) from "Available groups"
5. Click the arrow to move to "Chosen groups"
6. Click "Save"

### Programmatically:

```python
from django.contrib.auth.models import Group
from accounts.models import CustomUser

# Get or create groups
viewers_group, _ = Group.objects.get_or_create(name='Viewers')
editors_group, _ = Group.objects.get_or_create(name='Editors')
admins_group, _ = Group.objects.get_or_create(name='Admins')

# Assign user to a group
user = CustomUser.objects.get(username='john_doe')
user.groups.add(editors_group)
```

## Permission-Protected Views

### Views in accounts/views.py

#### 1. document_list (View Documents)

- **Permission Required:** `accounts.can_view`
- **Decorator:** `@permission_required('accounts.can_view', raise_exception=True)`
- **Access:** Viewers, Editors, Admins

#### 2. document_create (Create Document)

- **Permission Required:** `accounts.can_create`
- **Decorator:** `@permission_required('accounts.can_create', raise_exception=True)`
- **Access:** Editors, Admins

#### 3. document_edit (Edit Document)

- **Permission Required:** `accounts.can_edit`
- **Decorator:** `@permission_required('accounts.can_edit', raise_exception=True)`
- **Access:** Editors, Admins

#### 4. document_delete (Delete Document)

- **Permission Required:** `accounts.can_delete`
- **Decorator:** `@permission_required('accounts.can_delete', raise_exception=True)`
- **Access:** Admins only

## Testing the Permission System

### Test Case 1: Viewer User

```python
# Create a viewer user
viewer = CustomUser.objects.create_user(
    username='viewer_user',
    email='viewer@example.com',
    password='testpass123'
)
viewer.groups.add(Group.objects.get(name='Viewers'))

# Expected behavior:
# ✓ Can access document_list
# ✗ Cannot access document_create (403 Forbidden)
# ✗ Cannot access document_edit (403 Forbidden)
# ✗ Cannot access document_delete (403 Forbidden)
```

### Test Case 2: Editor User

```python
# Create an editor user
editor = CustomUser.objects.create_user(
    username='editor_user',
    email='editor@example.com',
    password='testpass123'
)
editor.groups.add(Group.objects.get(name='Editors'))

# Expected behavior:
# ✓ Can access document_list
# ✓ Can access document_create
# ✓ Can access document_edit
# ✗ Cannot access document_delete (403 Forbidden)
```

### Test Case 3: Admin User

```python
# Create an admin user
admin_user = CustomUser.objects.create_user(
    username='admin_user',
    email='admin@example.com',
    password='testpass123'
)
admin_user.groups.add(Group.objects.get(name='Admins'))

# Expected behavior:
# ✓ Can access document_list
# ✓ Can access document_create
# ✓ Can access document_edit
# ✓ Can access document_delete
```

## Migration Steps

After adding the Document model with custom permissions:

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (if not exists)
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## Security Notes

1. **raise_exception=True**: All permission decorators use `raise_exception=True` to return a 403 Forbidden response instead of redirecting to login page when permission is denied.

2. **Permission Naming**: Permissions follow Django's convention: `app_label.permission_codename`

   - Example: `accounts.can_view`

3. **Superuser Override**: Superusers automatically have all permissions, regardless of group membership.

4. **Multiple Groups**: Users can belong to multiple groups and will have the union of all permissions from their groups.

## Troubleshooting

### Permission Not Found Error

- Ensure migrations have been run: `python manage.py migrate`
- Check that the permission exists: `python manage.py shell`
  ```python
  from django.contrib.auth.models import Permission
  Permission.objects.filter(codename__startswith='can_')
  ```

### User Has Permission But Still Gets 403

- Verify the user is in the correct group
- Check that the group has the permission assigned
- Ensure the permission codename matches exactly (case-sensitive)

### Groups Not Appearing in Admin

- Ensure you're logged in as a superuser
- Check that `django.contrib.auth` is in INSTALLED_APPS

## Best Practices

1. **Least Privilege Principle**: Assign only the minimum permissions necessary for users to perform their tasks.

2. **Use Groups**: Always assign permissions to groups rather than individual users for easier management.

3. **Document Changes**: Keep this documentation updated when adding new permissions or modifying group structures.

4. **Regular Audits**: Periodically review user group memberships and permissions to ensure they're still appropriate.

5. **Testing**: Always test permission enforcement after making changes to ensure security is maintained.
