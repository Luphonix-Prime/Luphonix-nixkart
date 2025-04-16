import os
import django
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run([sys.executable, command], check=True)
        print(f"Successfully executed {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")
        sys.exit(1)

def main():
    # Set up Django environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
    django.setup()

    # Run migrations first
    print("Running migrations...")
    run_command('manage.py', 'migrate')

    # Fix sites configuration
    print("Fixing sites configuration...")
    run_command('fix_sites.py')

    # Create admin user
    print("Creating admin user...")
    run_command('create_admin.py')

    # Create sample users
    print("Creating sample users...")
    run_command('create_users.py')

    # Add sample data
    print("Adding sample data...")
    run_command('add_sample_data.py')

if __name__ == '__main__':
    main()
