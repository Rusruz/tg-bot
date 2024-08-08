__all__ = ("router",)

from aiogram import Router

from .commands import router as commands_router
from .user_messages import router as user_router

router = Router(name=__name__)

router.include_routers(
    commands_router,
    user_router,
)
