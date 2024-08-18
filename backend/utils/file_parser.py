def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'txt'}


def parse_log_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content
