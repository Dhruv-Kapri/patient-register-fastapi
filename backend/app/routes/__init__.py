from .home import router as home_router
from .about import router as about_router
from .view import router as view_router
from .patient import router as patient_router
from .sort import router as sort_router
from .edit import router as edit_router
from .create import router as create_router
from .delete import router as delete_router

all_routers = [
    home_router,
    about_router,
    view_router,
    patient_router,
    sort_router,
    edit_router,
    create_router,
    delete_router
]
