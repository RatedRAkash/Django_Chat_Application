import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chatApp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoChatServer.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()


# kon Type Protocol er jonno kon ROUTING use korbe sheita eikane define korbe
application = ProtocolTypeRouter({
    # HTTP protocols
    "http": django_asgi_app, #keu "http://" diya server ke Call dile ei ROUTE ee jabe
    'websocket':AuthMiddlewareStack( #keu "ws://" diya server ke Call dile ei ROUTE ee jabe
        URLRouter(
            chatApp.routing.websocket_urlpatterns
        )
    )
})