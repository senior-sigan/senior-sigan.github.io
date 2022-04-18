import os


def rename():
    for dir_name in os.listdir('_notes'):
        old_path = os.path.join('_notes', dir_name)
        dt = dir_name[:12]
        name = dir_name[12:]
        y, m, d = dt[:4], dt[4:6], dt[6:8]
        new_date = f"{y}-{m}-{d}"
        new_path = os.path.join('_notes', new_date+name)
        os.rename(old_path, new_path)


rename()
