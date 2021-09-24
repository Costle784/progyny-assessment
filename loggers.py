import logging
from pathlib import Path

parent_path = Path(__file__).parent.resolve()

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

stream_handler = logging.StreamHandler()

error_file_handler = logging.FileHandler(f'{parent_path}/storage/logs/error.log')
error_file_handler.setFormatter(formatter)
error_log = logging.getLogger('error_logger')
error_log.addHandler(error_file_handler)
error_log.addHandler(stream_handler)
error_log.setLevel(logging.ERROR)

app_log = logging.getLogger('app_logger')
app_file_handler = logging.FileHandler(f'{parent_path}/storage/logs/app.log')
app_file_handler.setFormatter(formatter)
app_log.addHandler(stream_handler)
app_log.addHandler(app_file_handler)
app_log.setLevel(logging.INFO)
