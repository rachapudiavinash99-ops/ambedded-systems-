import os
import zipfile

base_dir = r'D:\ambedded systems'
os.chdir(base_dir)

# Remove the previously generated fake file
if os.path.exists('backend/app/simulators/logic_core.py'):
    os.remove('backend/app/simulators/logic_core.py')

# Git commit the new modules
os.system('git rm backend/app/simulators/logic_core.py --ignore-unmatch')
os.system('git add backend/app/embedded_modules/')
os.system('git commit -m "Add embedded hardware firmware modules"')

def create_zip():
    zip_path = r'D:\ambedded_systems_submission_final.zip'
    print(f'Creating zip at {zip_path}')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk('.'):
            for file in files:
                file_path = os.path.join(root, file)
                if 'ambedded_systems_submission' in file_path or file_path.endswith('.zip'):
                    continue
                zipf.write(file_path, arcname=os.path.relpath(file_path, '.'))
    print('Zip created.')

create_zip()
