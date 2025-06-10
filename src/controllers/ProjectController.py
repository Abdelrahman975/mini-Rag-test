from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os

class ProjectController(BaseController):

    def __init__(self):
        super().__init__()

    def get_porject_path(self,project_id:str):
        porject_dir = os.path.join(
            self.files_dir,
            project_id
        )

        if not os.path.exists(porject_dir):
            os.makedirs(porject_dir)

        return porject_dir
