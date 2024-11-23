import os
import shutil
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.timezone import now


class Command(BaseCommand):
    help = 'Copies templates and static files from the package into the project.'

    def add_arguments(self, parser):
        # Add event_year as an argument to be passed by the user
        parser.add_argument(
            '--event-year', type=str, required=True, help='Specify the event year for the template folder.'
        )

    def handle(self, *args, **kwargs):
        event_year = kwargs['event_year']

        # Get the paths for the templates and static directories in the Django project
        templates_dir = settings.TEMPLATES[0]['DIRS'][0]
        static_dir = settings.STATICFILES_DIRS[0]

        # Path for the new event year folder inside templates
        event_year_folder = os.path.join(templates_dir, f"event_{event_year}")
        os.makedirs(event_year_folder, exist_ok=True)

        # Copy templates from the package to the event year folder
        package_templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
        self.copy_files(package_templates_dir, event_year_folder)

        # Copy static files from the package to the static directory
        package_static_dir = os.path.join(os.path.dirname(__file__), 'static')  # Your package's static directory
        self.copy_files(package_static_dir, static_dir)

        self.stdout.write(self.style.SUCCESS(f'Successfully copied files for event year {event_year}'))

    def copy_files(self, src_dir, dest_dir):
        """Helper function to copy files from source to destination."""
        for root, dirs, files in os.walk(src_dir):
            # Get relative path from the source directory
            relative_path = os.path.relpath(root, src_dir)
            destination_dir = os.path.join(dest_dir, relative_path)

            # Ensure destination directory exists
            os.makedirs(destination_dir, exist_ok=True)

            for file_name in files:
                # For template files, rename them to default-{filename}
                if src_dir.endswith('templates'):
                    file_name = f'default-{file_name}'
                # Copy the file
                src_file = os.path.join(root, file_name)
                dest_file = os.path.join(destination_dir, file_name)

                # Copy the file
                shutil.copy(src_file, dest_file)
