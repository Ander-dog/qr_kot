from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charityproject import (CharityProjectCreate,
                                        CharityProjectUpdate)


class CRUDCharityProject(CRUDBase[
    CharityProject,
    CharityProjectCreate,
    CharityProjectUpdate
]):
    pass


charityproject_crud = CRUDCharityProject(CharityProject)
