from .commands import router as commands_router
from .auth import router as auth_router
from .text_handlers import router as text_router
from .admin_panel import router as admin_router
from .callbackquery import router as callback_router

__all__ = ["commands_router",
           "auth_router",
           "text_router",
           "admin_router",
           "callback_router"]